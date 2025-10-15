## Definição Formal das Métricas

### 1. Overspend Index (OI)

**Fórmula:**
\[
OI_t = \frac{Gasto_t}{\epsilon + \text{Média}(Gasto_{t-1}, Gasto_{t-2}, Gasto_{t-3})}
\]

**Interpretação:**
- \( OI > 1.25 \) → gasto 25 % acima da média recente  
- \( OI < 0.75 \) → queda acentuada no consumo  

---

### 2. Large Transaction Z-Score (LTZ)

**Fórmula:**
\[
LTZ = \frac{Valor - \mu_{\text{categoria}}}{\sigma_{\text{categoria}} + \epsilon}
\]

**Interpretação:**
- \( |LTZ| \ge 3 \) → transação atípica  
- Permite detectar gastos muito acima (ou abaixo) do padrão da categoria