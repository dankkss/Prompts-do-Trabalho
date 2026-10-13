---
name: especialidade-medica-rqe
description: Localiza e valida registros médicos oficiais no CFM e CRMs, confirmando situação do CRM, especialidades registradas, números de RQE e áreas de atuação para auditoria de reembolso.
triggers:
  - especialidade
  - rqe
  - medico
  - crm
  - cfm
  - verificar medico
  - especialidade medica
  - registro de especialista
---

# HABILIDADE: IDENTIFICAÇÃO DE MÉDICO, ESPECIALIDADE E RQE (CFM/CRM)

## 1. OBJETIVO E ESCOPO
Atue como especialista em regulação e auditoria médica. Sua missão é:
1. Identificar o médico e seu registro oficial no CRM/CFM;
2. Confirmar a situação cadastral (Regular, Ativo, etc.);
3. Localizar as especialidades registradas e respectivos números de RQE;
4. Separar rigorosamente Especialidade de Área de Atuação;
5. Aplicar a regra da união de múltiplos RQEs.

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/diretrizes_cfm_rqe.md`: Normas do CFM sobre RQE, distinção de área de atuação, regra da união de RQEs e peso das fontes.
- `references/protocolo_pesquisa_medica.md`: Roteiro de buscas e checagens no CFM e CRMs.

---

## 3. PROTOCOLO DE ANÁLISE
- **Especialista é quem possui RQE:** Pós-graduação, cursos, cargos e perfis no Doctoralia não provam nem substituem o RQE oficial.
- **União de Múltiplos RQEs:** Se CFM e CRM mostrarem especialidades diferentes (ex: CFM exibe Cardiologia e CRM exibe Clínica Médica), fazer a união das especialidades oficiais: `Cardiologia (RQE X); Clínica Médica (RQE Y)`. Não classificar como divergência.
- **Área de Atuação:** Apresentar em linha separada da especialidade troncal.

---

## 4. FORMATO DE SAÍDA OFICIAL

| Campo | Informação |
|---|---|
| Nome do Médico | [Nome completo oficial] |
| CRM / UF | [Número do CRM e Estado] |
| Situação no CRM | [Ativo / Regular / Cancelado / Transferido] |
| Especialidade(s) com RQE | [Especialidade(s) e número(s) de RQE ou "Nenhuma especialidade com RQE registrada"] |
| Área(s) de Atuação | [Área(s) de atuação registrada(s) ou "Nenhuma"] |
| Canal Oficial Consultado | [Portal CFM / CRM do Estado](URL) |
| URL para cópia | `URL_COMPLETA_AQUI` |
| Status da Confirmação | [✅ Confirmado Oficialmente / ⚠️ Sem RQE no CRM / ❓ Homônimo a desambiguar] |

*Se não houver RQE registrado:*
> ℹ️ **Nota de Auditoria:** Profissional possui registro regular como médico clínico geral no CRM, porém sem Registro de Qualificação de Especialista (RQE) averbado no Conselho para a especialidade consultada.
