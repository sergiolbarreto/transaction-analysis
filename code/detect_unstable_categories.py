import pandas as pd
import json

def detect_unstable_categories(csv_path, inactive_threshold=10.0):
    """
    Detects categories with non-stable Overspend Index (OI) behavior from a transaction CSV.

    A category is classified as:
        - "upward"   → OI > 1.05 (spending increased)
        - "downward" → OI < 0.95 (spending decreased)
        - "inactive" → last month's total spending < inactive_threshold
        - "stable"   → otherwise (not returned here)

    Parameters:
        csv_path (str): Path to the transaction CSV file.
        inactive_threshold (float): Minimum monthly spending to consider category active.

    Returns:
        JSON string with only the non-stable categories.
    """

    epsilon = 1e-9

    # Load and preprocess data
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

    # Keep only debit (outgoing) transactions
    df = df[df['amount'] < 0].copy()
    df['amount'] = df['amount'].abs()

    # Extract year-month
    df['year_month'] = df['date'].dt.to_period('M')

    # Monthly spending by category
    monthly = (
        df.groupby(['category', 'year_month'])['amount']
        .sum()
        .reset_index()
        .sort_values(['category', 'year_month'])
    )

    # Rolling mean of past 3 months
    monthly['rolling_mean'] = (
        monthly.groupby('category')['amount']
        .apply(lambda x: x.shift(1).rolling(3, min_periods=3).mean())
        .reset_index(level=0, drop=True)
    )

    # Calculate Overspend Index
    monthly['OI'] = monthly['amount'] / (monthly['rolling_mean'] + epsilon)

    # Get latest record per category
    latest = monthly.groupby('category').tail(1).copy()

    # Classify trend safely
    def classify_trend(row):
        if row['amount'] < inactive_threshold:
            return "inactive"
        elif row['OI'] > 1.05:
            return "upward"
        elif row['OI'] < 0.95:
            return "downward"
        else:
            return "stable"

    latest.loc[:, 'trend'] = latest.apply(classify_trend, axis=1)

    # Keep only non-stable categories
    unstable = latest[latest['trend'] != 'stable']

    # Build list of results
    results = []
    for _, row in unstable.iterrows():
        results.append({
            "metric_name": "Overspend Index",
            "category": row['category'],
            "year_month": str(row['year_month']),
            "value": round(float(row['OI']), 2),
            "trend": row['trend']
        })

    return json.dumps(results, indent=4, ensure_ascii=False)