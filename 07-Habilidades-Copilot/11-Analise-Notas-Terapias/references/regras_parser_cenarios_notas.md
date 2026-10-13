# PARSER DE ENTRADA, REGRAS DE DATA E CENÁRIOS DE SINISTRO

Este documento define como interpretar mensagens de analistas no primeiro turno e estruturar os dados para emissão da nota técnica.

---

## 1. PARSER AUTOMÁTICO DE ENTRADA CURTA
O auditor deve aceitar entradas compactas sem exigir rótulos formais:
- **Token de CID:** Letra seguida de 2 a 4 números (ex: `E66`, `E11`, `F840`, `M545`) => Associar ao Diagnóstico / CID.
- **Data (DD/MM/AAAA):** Associar conforme a regra crítica abaixo.
- **Número com token de sessão:** Ex: `4 sessões`, `5 sessoes`, `6 util` => Quantidade utilizada / realizada.
- **Padrão de Sinistro:** `AAAA.SEQUENCIA.DD` (ex: `2026.001234.01`) => Número do sinistro.

---

## 2. REGRA CRÍTICA DE INTERPRETAÇÃO DE DATA
A interpretação de uma data isolada depende obrigatoriamente do TIPO de serviço:
- **NUTRIÇÃO:** Qualquer data isolada fornecida pelo analista deve ser interpretada como **DATA DA VIGÊNCIA** (aniversário da apólice), salvo indicação expressa em contrário.
- **DEMAIS TERAPIAS:** Qualquer data isolada deve ser interpretada como **DATA DO PEDIDO MÉDICO**, salvo indicação expressa em contrário.
- **PROIBIÇÃO:** Nunca trocar esses rótulos. Se houver mais de uma data e o contexto não permitir diferenciação segura, adotar a mais compatível e registrar a ressalva em `Validação do analista`.

---

## 3. DEFINIÇÃO DE CENÁRIOS
- **Cenário 01:** Quando houver número de sinistro informado na entrada (formato `AAAA.SEQUENCIA.DD`).
- **Cenário 02:** Quando NÃO houver número de sinistro informado na entrada.
- **Regra de Não-Interrogação:** Nunca pergunte ao usuário se existe sinistro antes de emitir a nota. Se vier com sinistro, aplique Cenário 01; se vier sem, aplique Cenário 02 imediatamente.

---

## 4. FORMATO MULTIPLATAFORMA
A nota técnica deve ser entregue integralmente dentro de um bloco de código ````text ``` para permitir que o analista de reembolso copie e cole diretamente no sistema corporativo (SCAM / Sisreg) sem quebras de formatação Markdown ou HTML.
