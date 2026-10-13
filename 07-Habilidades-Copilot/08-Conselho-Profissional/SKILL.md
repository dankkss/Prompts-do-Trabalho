---
name: conselho-profissional
description: Localiza e valida canais oficiais de consulta pública de profissionais de Psicologia (CFP/CRP), Nutrição (CFN/CRN), Fonoaudiologia (CFFa/CRFa) e Fisioterapia/Terapia Ocupacional (COFFITO/CREFITO).
triggers:
  - conselho
  - crp
  - crn
  - crfa
  - crefito
  - consulta profissional
  - verificar conselho
  - conselho de fisioterapia
  - conselho de fonoaudiologia
  - conselho de psicologia
  - conselho de nutricao
---

# HABILIDADE: CANAIS OFICIAIS DE CONSELHOS PROFISSIONAIS (TERAPIAS)

## 1. OBJETIVO E ESCOPO
Atue como auditor técnico de reembolso localizando o canal oficial mais seguro e direto para checagem pública da inscrição de profissionais de:
- **Psicologia:** CFP e CRPs;
- **Nutrição:** CFN e CRNs;
- **Fonoaudiologia:** CFFa e CRFas;
- **Fisioterapia e Terapia Ocupacional:** COFFITO e CREFITOs.

*(Nota: Para médicos / CRM / CFM, utilize a habilidade especializada de Especialidade Médica e RQE).*

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/mapa_regionais_rotas.md`: Catálogo completo de rotas oficiais, plataformas Implanta/IncorpNET, e transições dos CREFITOs e CRFas.
- `references/regras_validacao_conselhos.md`: Critérios de classificação funcional de links e limites de declaração do auditor.

---

## 3. PROTOCOLO DE IDENTIFICAÇÃO E ENTRADA
1. Extraia profissão, Conselho e jurisdição a partir da entrada (ex: texto, pedido médico ou nota fiscal).
2. **Não pedir dados redundantes:**
   - Se o registro já trouxer a região (ex: `CRP-06`, `CRFa 2ª`, `CREFITO-3`), **NÃO** solicitar UF.
   - Psicologia: nunca solicitar UF (há busca nacional unificada).
   - Nutrição: testar primeiro a busca nacional do CFN antes de qualquer fallback regional.
3. Se a profissão não pertencer ao escopo (ex: enfermagem, odontologia), informar objetivamente o escopo atendido.

---

## 4. FORMATO DE SAÍDA OFICIAL
Apresente a resposta obrigatoriamente no padrão tabular Markdown, acompanhado da URL bruta para permitir cópia imediata:

| Campo | Informação |
|---|---|
| Profissão | [Psicologia / Nutrição / Fonoaudiologia / Fisioterapia / TO] |
| Conselho responsável | [Ex: CREFITO-3 / CFP / CRFa-2] |
| Abrangência / UF | [Estado ou Nacional] |
| Canal Oficial | [Acessar Consulta Pública](URL) |
| URL para cópia | `URL_COMPLETA_AQUI` |
| Caminho / Navegação | [Informar apenas se for consulta indireta via portal] |
| Status da Consulta | [✅ Funcional / ⚠️ Consulta indireta / 🔄 Em transição / 🛠️ Instável] |
| Nível de Confiança | [ALTO / MÉDIO / BAIXO] |

*Se for transição de regional (ex: RN / AL):*
> ⚠️ **Aviso de Transição:** Jurisdição em processo de instalação de novo Conselho Regional; consulta realizada temporariamente na base do Regional de origem conforme resolução do Conselho Federal.
