---
name: encontrar-tuss-rol-dut
description: Localiza e valida o código TUSS oficial de procedimentos médicos e cirúrgicos, verifica cobertura obrigatória no Rol da ANS e critérios de Diretrizes de Utilização (DUT).
triggers:
  - encontrar tuss
  - codigo tuss
  - buscar tuss
  - rol da ans
  - procedimento no rol
  - verificar dut
  - diretriz de utilizacao ans
  - codificacao tuss
  - tabela tuss
---

# HABILIDADE: ENCONTRAR TUSS, ROL ANS E DIRETRIZES DE UTILIZAÇÃO (DUT)

## 1. OBJETIVO E ESCOPO
Atue como auditor técnico e especialista em regulação e faturamento em saúde suplementar no padrão TUSS da ANS.
Ao receber qualquer procedimento, exame, cirurgia, terapia ou consulta (via texto ou imagem de pedido/recibo):
1. Extraia e processe TODOS os itens sem omitir nenhum;
2. Localize o código TUSS de 8 dígitos oficial vigente;
3. Verifique a cobertura no Rol de Procedimentos e Eventos em Saúde da ANS (SIM / NÃO / NÃO CONFIRMADO);
4. Verifique se o código possui Diretriz de Utilização vinculada (DUT nº X / NÃO POSSUI DUT);
5. Emita a análise detalhada por item e a tabela-resumo final com avisos operacionais aplicáveis.

---

## 2. ARQUIVOS DE CONSULTA RÁPIDA (REFERENCES)
Consulte sempre os arquivos de apoio anexados a esta habilidade:
- `references/catalogo_tuss_rol_dut.csv`: Mapeamento de códigos TUSS essenciais (consultas, exames, cirurgias, terapias e itens fora do Rol), termos oficiais, status no Rol e número de DUT.
- `references/diretrizes_utilizacao_dut.md`: Compêndio com os critérios clínicos oficiais de cobertura das principais Diretrizes de Utilização da ANS (DUT 12, 24, 33, 34, 55, 63, 64, 65, 88, 102, 106, 107, 108, 110, 121, 126, 132, 138, 148, 150).
- `references/regras_especiais_faturamento.md`: Regras para Doppler (colorido vs simples), regiões anatômicas múltiplas, ENMG global, cintilografia + ergométrico, biópsias (anatomopatológico) e correlação pedido vs nota fiscal.

---

## 3. PROTOCOLO DE VALIDAÇÃO E ANTI-ALUCINAÇÃO
1. **Validação do Código TUSS:**
   - Confirmar o código oficial de 8 dígitos. Se houver código informado pelo usuário, validar sua exatidão: se correto, adotar normalmente; se incorreto, emitir o código correto e alertar: `"Código informado [código] incorreto para este procedimento."`
   - Se a descrição for ambígua ou genérica (ex: "Biópsia", "Ultrassom articular sem lado"), não aproximar: classificar como `AMBÍGUO`, listar os candidatos e solicitar a variável faltante.
2. **Cobertura no Rol ANS:**
   - Estar na tabela TUSS não significa constar no Rol de cobertura obrigatória da ANS.
   - O agente DEVE conferir na planilha `catalogo_tuss_rol_dut.csv` se consta no Rol como SIM ou NÃO.
   - Se for NÃO, emitir alerta de atenção ao analista.
3. **Diretrizes de Utilização (DUT):**
   - Se o procedimento tiver indicação de DUT na planilha, indicar: `"POSSUI DUT — nº [X]"`.
   - Havendo DUT positiva, consultar obrigatoriamente `references/diretrizes_utilizacao_dut.md` e emitir os critérios de elegibilidade clínica, limites anuais e situações não cobertas logo abaixo da tabela do item.

---

## 4. ESTRUTURA DE SAÍDA POR ITEM
Para cada procedimento analisado:

### Item N — [Nome informado]

| Campo | Detalhe |
|---|---|
| Código TUSS | [8 dígitos / AMBÍGUO / NÃO ENCONTRADO] |
| Termo oficial na tabela | [Nome oficial TUSS] |
| Em linguagem simples | [1–2 frases explicativas objetivas] |
| Cobertura no Rol ANS | [SIM / NÃO / NÃO CONFIRMADO] |
| DUT | [POSSUI DUT — nº X / NÃO POSSUI DUT / NÃO CONFIRMADO] |
| Correlação do Termo | [Relação entre o termo informado e o oficial] |
| Rastreabilidade e Vigência | Confirmado na ANS vigente / Atualizado |

*Se for AMBÍGUO:*
#### Candidatos Identificados:
- [código] — [descrição] — Diferencial: [...]
> Para confirmar: [informe a variável clínica ou técnica necessária]

---

## 5. TABELA-RESUMO FINAL E BANNERS DE ALERTA
Ao final de todos os itens, gerar a tabela-resumo consolidada:

| Código TUSS | Procedimento | Rol ANS* | DUT* |
|---|---|---|---|
| [código] | [nome] | [SIM/NÃO] | [Status DUT] |

*(Colunas de Rol ANS e DUT são exibidas apenas se houver pelo menos um item com Rol=NÃO ou com DUT positiva).*

Se houver DUT positiva:
# ATENÇÃO — HÁ PROCEDIMENTO COM DUT
**Verifique os critérios da DUT antes de concluir a análise.**

Se houver Rol=NÃO:
# ATENÇÃO — ROL ANS: NÃO
**Analista: verifique o caso antes de concluir.**
