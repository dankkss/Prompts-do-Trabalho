# MANUAL DE CÁLCULO REVERSO DE VACINA NO SISTEMA SCAM

Este guia estabelece a formulação matemática, os critérios de leitura de tela e a formatação numérica do cálculo reverso para liberação de vacinas no sistema SCAM.

---

## 1. PARÂMETROS E DEFINIÇÃO DE VARIÁVEIS
- **Valor X:** O valor monetário total liberado para a vacina sob as condições do contrato (fornecido expressamente pelo analista no chat).
  * *Atenção:* Nunca extrair ou estimar o Valor X a partir do print da tela. O Valor X é sempre informado pelo usuário.
- **Variáveis Extraídas da Imagem (Demonstrativo do Cálculo):**
  * `A` = Quantidade (rótulo exato: "Quantidade");
  * `B` = Fator de Reembolso (rótulo exato: "Fator de Reembolso");
  * `D` = Vlr. Unit. Coef. (rótulo exato: "Vlr. Unit. Coef.").
- **Regra de Ausência ou Ilegibilidade:** Se A, B ou D estiver cortado, ilegível ou ausente na imagem, não estimar: informar qual campo não pôde ser lido e solicitar novo print.
- **Divisor Zero:** Se A, B ou D for zero, abortar o cálculo informando a impossibilidade de divisão por zero.

---

## 2. FORMULAÇÃO MATEMÁTICA
O cálculo do coeficiente unitário C aplica a equação:

$$C = \frac{\text{Valor X}}{A \times B \times D}$$

Ou passo a passo: `C = Valor X ÷ A ÷ B ÷ D`.

### Regras de Precisão e Arredondamento:
1. Utilizar ponto flutuante de máxima precisão para todos os cálculos intermediários;
2. **NÃO arredondar** A, B, D ou resultados intermediários;
3. Arredondar **exclusivamente o resultado final de C para exatamente 6 casas decimais**;
4. No resultado final, usar **obrigatoriamente vírgula (`,`) como separador decimal** (nunca ponto);
5. Preservar zeros à direita até completar 6 casas decimais (ex: `1,500000`, `0,123450`).

---

## 3. FORMATO DE SAÍDA OFICIAL
Apresentar os dados lidos e o Item C calculado isolado dentro de um bloco de código ````text ```:

Valor liberado para a vacina nas condições do contrato (Valor X): [valor]

A — Quantidade: [valor lido]
B — Fator de Reembolso: [valor lido]
D — Vlr. Unit. Coef.: [valor lido]

Item C calculado:
```text
0,000000
```

*(Dentro do bloco de código, não colocar "C =", símbolos de moeda ou texto; apenas o número puro com 6 casas decimais e vírgula).*
