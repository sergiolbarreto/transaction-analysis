# 🧾 Transaction Analysis

Este projeto realiza uma **análise automatizada de transações financeiras**, com o objetivo de identificar:

- 📊 **Padrões de consumo** por categoria  
- ⚠️ **Outliers** (gastos atípicos)  
- 📈 **Mudanças de comportamento** em categorias de gasto ao longo do tempo  

O projeto combina **métricas estatísticas** e **indicadores de tendência** para construir relatórios interpretáveis, ideais para monitoramento financeiro pessoal ou corporativo.

---

## 🧠 Metodologia

Durante a execução, o código realiza as seguintes etapas:

1. **Leitura e pré-processamento** do dataset de transações.  
2. **Cálculo de estatísticas descritivas e sazonalidade** (média, desvio padrão, coeficiente de variação).  
3. **Detecção de outliers** via método IQR (Interquartile Range).  
4. **Proposta de ferramenta acionável (fluxo de alertas)** 
5. **Identificação de categorias instáveis** (picos ou quedas bruscas).  
6. **Geração de saídas** em formato `.csv`, `.png` e `.json`.

---

## 🚀 Como reproduzir os resultados

Para executar a análise e gerar os mesmos resultados, basta rodar o notebook:

### 1. Clonar o repositório
```bash
git clone https://github.com/sergiolbarreto/transaction-analysis.git
cd transaction-analysis
```
### 2. Instalar dependências
```bash
pip install pandas numpy matplotlib seaborn
```
### 3. Abrir o notebook
Abra o arquivo transaction_analysis.ipynb em:
* Google Colab
* Localmente com Jupyter Notebook:
```bash
jupyter notebook transaction_analysis.ipynb
```

## ⚠️ Atenção à célula de configuração do CSV

No início do notebook há uma célula de configuração semelhante a:

```python
# Paths
BASE = ""
CSV_PATH = f"{BASE}/transactions.csv"
```
Preencha o caminho em `BASE` caso precise alterar a localização do arquivo transactions.csv antes de executar o restante do notebook.

## 📈 Saídas esperadas

- Relatórios `.csv` com estatísticas e outliers  
- Arquivo `.json` com categorias não estáveis  
- Gráficos `.png` de sazonalidade e variação de gasto

### 🧭 Próximos Passos

Como evolução natural da análise, os próximos passos seriam:

1. **Personalização de métricas** — adaptar indicadores (variação, outliers, sazonalidade) ao perfil e comportamento de cada usuário.  
2. **Modelos preditivos** — aplicar séries temporais para prever gastos futuros e sugerir ações preventivas.  
3. **Alertas inteligentes** — integrar as métricas a um sistema de alertas proativo e configurável.  

Essas etapas tornariam o sistema mais **inteligente, proativo e personalizado**.

