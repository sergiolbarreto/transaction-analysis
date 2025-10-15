##  3. Proposta de Ferramenta Acionável

###  Fluxo de Interação

1. **Coleta diária de transações**  
   - O sistema importa automaticamente as novas movimentações do usuário (ex: app bancário ou plataforma de controle financeiro).  

2. **Cálculo automático das métricas**  
   - Para cada categoria e transação:
     - Calcula o **Overspend Index (OI)** → compara o gasto atual com a média dos 3 meses anteriores.  
     - Calcula o **Large Transaction Z-Score (LTZ)** → identifica transações muito acima do padrão da categoria.  

3. **Detecção de eventos anômalos**  
   - Se **OI > 1.25**, o sistema detecta pico de gasto.  
   - Se **|LTZ| ≥ 3**, o sistema detecta transação atípica.  

4. **Geração de alerta**  
   - O sistema envia **notificação push ou e-mail** imediatamente após a detecção (ou em resumo diário).  

5. **Visualização no painel**  
   - O usuário acessa um painel que exibe:
     - Categoria afetada  
     - Valor gasto e média anterior  
     - Tipo de alerta (pico de gasto / transação fora do padrão)  
     - Sugestão de ação (ex: revisar assinatura, confirmar despesa, ajustar orçamento)

6. **Ação do usuário**  
   - O usuário pode **confirmar** a despesa como legítima, **categorizar** novamente, ou **definir novo limite**.

---

### ⚙️ Parâmetros Configuráveis

- **Limite de OI**: valor de alerta (ex: 1.25 padrão, ajustável pelo usuário).  
- **Limite de LTZ**: nível de sensibilidade (ex: 2.5, 3.0).  
- **Frequência de alertas**: imediata, diária ou semanal.  
- **Categorias monitoradas**: o usuário pode ativar/desativar alertas por tipo de gasto.  
- **Canal de notificação**: e-mail, push, SMS.

---

### Exemplo de Alerta ao Usuário

> **📈 Alerta de Gasto Atípico — Transferência PIX**  
> Seu gasto com **Transferência - PIX** neste mês está **4,2× acima da média recente**.  
>
> 💰 **Valor:** R$ 2.480,00  
> 📅 **Média dos 3 últimos meses:** R$ 590,00  
> ⚠️ Esse aumento pode indicar uma transação pontual ou um novo padrão de consumo.  
>
> ➜ **Sugestão:** revise a transação e, se for um gasto recorrente, atualize seu limite de categoria.
