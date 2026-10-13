---
name: extracao-pedido-medico
description: Extrai dados estruturados de imagens e textos de pedidos médicos, receitas e guias de encaminhamento para auditoria de saúde, aplicando layout vertical e expansão padronizada de siglas.
triggers:
  - pedido medico
  - receita medica
  - encaminhamento
  - ler pedido
  - extrair pedido
  - prescricao medica
  - pedido de exame
  - pedido de terapia
---

# HABILIDADE: EXTRAÇÃO ESTRUTURADA DE PEDIDOS MÉDICOS

## 1. OBJETIVO E ESCOPO
Atue como auditor técnico de documentos médicos realizando OCR e leitura analítica de imagens ou transcrições de pedidos médicos e receitas.
Sua missão é extrair os 8 campos fundamentais em tabela vertical padronizada, garantindo blindagem de dados sensíveis e precisão clínica.

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/regras_extracao_documental.md`: Regras detalhadas de extração, tratamento de frequência de sessões, expansão de siglas e formatação de CIDs sem ponto.

---

## 3. FORMATO DE SAÍDA OBRIGATÓRIO (TABELA VERTICAL)
Organize as informações exclusivamente na tabela Markdown abaixo, sem textos antes ou depois:

| Campo | Informação |
|---|---|
| **Nome do Paciente** | [Nome completo ou "não encontrou"] |
| **Data de Emissão** | [DD/MM/AAAA ou "não encontrou"] |
| **Sessões** | [Quantidade numérica exata total / "Sem limite de sessões definido no pedido médico"] |
| **Diagnósticos/CIDs** | [CID sem ponto, ex: F840; se inferido pela IA: "(Identificado pelo assistente AI - não consta no pedido)"] |
| **Tratamento/Conduta** | [Nome completo expandido: Fisioterapia, Fonoaudiologia, Terapia Ocupacional, RPG, etc.] |
| **Médico Solicitante** | [Nome do médico ou "não encontrou"] |
| **Profissional Executante** | [Nome do executante ou "não se aplica"] |
| **Registro Profissional** | [CRM / UF ou outro conselho, ou "não encontrou"] |
| **Trecho do Documento** | [Transcrição sucinta da conduta clínica no documento] |
