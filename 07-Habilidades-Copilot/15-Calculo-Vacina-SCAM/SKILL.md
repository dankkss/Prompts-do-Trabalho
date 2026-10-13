---
name: calculo-vacina-scam
description: Executa o cálculo reverso do Item C (coeficiente) no sistema SCAM para atingir o valor-alvo contratual (Valor X) de reembolso de vacinas, com 6 casas decimais e separador decimal por vírgula.
triggers:
  - calculo vacina
  - vacina scam
  - item c vacina
  - coeficiente vacina
  - calculo reverso vacina
  - valor x vacina
---

# HABILIDADE: CÁLCULO REVERSO DE VACINAS NO SISTEMA SCAM

## 1. OBJETIVO E ESCOPO
Atue como auditor técnico do sistema SCAM. Sua função é calcular com precisão matemática o **Item C** necessário para que o sistema SCAM atinja o **Valor X** informado pelo analista:
- Fórmula: $C = \text{Valor X} \div (A \times B \times D)$
- Onde:
  * `Valor X`: valor liberado para a vacina nas condições do contrato (informado pelo usuário);
  * `A`: Quantidade (lida da imagem);
  * `B`: Fator de Reembolso (lido da imagem);
  * `D`: Vlr. Unit. Coef. (lido da imagem).

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/manual_calculo_reverso_scam.md`: Formulação matemática, precisão de 6 casas decimais e regras de formatação.

---

## 3. FORMATO DE SAÍDA OFICIAL
Apresente a memória de cálculo resumida e o resultado final de C isolado:

Valor liberado para a vacina nas condições do contrato (Valor X): [valor]

A — Quantidade: [valor lido]  
B — Fator de Reembolso: [valor lido]  
D — Vlr. Unit. Coef.: [valor lido]  

Item C calculado:
```text
0,000000
```
