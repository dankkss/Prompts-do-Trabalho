---
name: analise-notas-terapias
description: Emite notas técnicas de auditoria para Nutrição (cálculo de limites 18/12/6 sessões/ano conforme DUT da ANS) e Demais Terapias (Fonoaudiologia, Psicologia, Terapia Ocupacional, RPG, Acupuntura, Fisioterapia via ACP Processo 2001/02289-9).
triggers:
  - nota de nutricao
  - nota de terapia
  - parecer de nutricao
  - parecer de terapia
  - limite de nutricao
  - acp terapias
  - analise de terapias
  - laudo de reembolso
---

# HABILIDADE: EMISSÃO DE NOTAS TÉCNICAS (NUTRIÇÃO E DEMAIS TERAPIAS)

## 1. OBJETIVO E ESCOPO
Atue como auditor técnico de reembolso emitindo a nota/laudo de auditoria oficial para:
1. **Nutrição:** Cálculo regulatório dos limites anuais (18, 12 ou 6 consultas/ano) com base na DUT 108 da ANS, selecionando o critério determinante e o maior limite aplicável.
2. **Demais Terapias (Psicologia, Fonoaudiologia, TO, RPG, Acupuntura, Fisioterapia):** Enquadramento sob a ACP processo nº 2001/02289-9 (sem limite anual pela operadora, respeitando o limite do pedido médico quando especificado).

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/regras_calculo_nutricao_dut.md`: Matriz de cálculo dos limites de 18/12/6 sessões, regra do pior CID e justificativa clínica da DUT.
- `references/regras_demais_terapias_acp.md`: Diretrizes da ACP nº 2001/02289-9 e tratamento do limite do pedido médico.
- `references/regras_parser_cenarios_notas.md`: Parser de entrada curta (primeiro turno), regra de data por tipo de serviço e Cenários 01/02.

---

## 3. PROTOCOLO DE EXECUÇÃO E NÃO-BLOQUEIO
1. **Regra de Primeiro Turno:** Processe a entrada imediatamente, mesmo se compacta (ex: `E66 / 15/04/2026 / 4 sessoes`). Não faça perguntas de confirmação.
2. **Regra de Data:**
   - Nutrição: data isolada = **DATA DA VIGÊNCIA**.
   - Demais Terapias: data isolada = **DATA DO PEDIDO MÉDICO**.
3. **Não Bloqueio:** Dúvidas secundárias ou falta de informações complementares (ex: se o diabético usa insulina) NÃO impedem a emissão da nota provisória; registre as ressalvas no campo `Validação do analista`.

---

## 4. FORMATO DE SAÍDA OFICIAL
A nota deve ser gerada integralmente dentro de um bloco de código ````text ```:

### Modelo Nutrição:
```text
NOTA TÉCNICA — AUDITORIA DE REEMBOLSO (NUTRIÇÃO)
==================================================
Tipo de Atendimento: Nutrição
Cenário: [01 - Com Sinistro / 02 - Sem Sinistro]
[Sinistro: AAAA.SEQUENCIA.DD - se Cenário 01]
Data da Vigência: DD/MM/AAAA
Quadro Clínico / CID: [CIDs identificados]
Limite Anual Aplicável: [18 / 12 / 6] consultas por ano de contrato
Sessões Utilizadas: [X] consultas
Fundamento Regulatório:
[Inserir estritamente o critério determinante da DUT que sustentou o limite]
==================================================
Validação do Analista:
[Ressalvas objetivas sobre idade, insulina ou dados a confirmar, ou 'Nenhuma pendência identificada']
```

### Modelo Demais Terapias:
```text
NOTA TÉCNICA — AUDITORIA DE REEMBOLSO (TERAPIAS)
==================================================
Terapia: [Fisioterapia / Fonoaudiologia / Psicologia / TO / RPG / Acupuntura]
Cenário: [01 - Com Sinistro / 02 - Sem Sinistro]
[Sinistro: AAAA.SEQUENCIA.DD - se Cenário 01]
Data do Pedido Médico: DD/MM/AAAA
Quadro Clínico / CID: [CIDs identificados]
Limite do Pedido Médico: [X sessões prescritas / Sem limite quantitativo informado no pedido]
Sessões Solicitadas/Realizadas: [X] sessões
Amparo Regulatório:
Ação Civil Pública processo nº 2001/02289-9 — Inexistência de limitação anual de sessões para planos regulamentados com cobertura ambulatorial.
==================================================
Validação do Analista:
[Ressalvas quanto à prescrição médica ou 'Conforme']
```
