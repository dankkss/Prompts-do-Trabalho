# PROTOCOLO DE PESQUISA E CONSULTA DE MÉDICOS NO CFM/CRM

Este guia orienta o método de consulta e verificação de dados de médicos para auditoria de sinistros e reembolso.

---

## 1. EXTRAÇÃO DE PARÂMETROS
O auditor deve reconhecer automaticamente os padrões comuns de CRM:
- `CRM-SP 12345`
- `CRM 12345 SP`
- `12345/SP`
- `CRM/SP 12345`
- `12345 SP`

---

## 2. ETAPAS DA PESQUISA NA WEB
1. **Etapa A — Identidade Oficial:**
   - Buscar combinações exatas: `"NOME DO MÉDICO" "CRM"` e `"NOME DO MÉDICO" "CRM" "UF"`.
   - Adicionar o domínio oficial: `site:portal.cfm.org.br "NOME"` ou `site:portal.cfm.org.br "CRM"`.
2. **Etapa B — Validação da Correspondência:**
   - Confirmar se o registro localizado pertence à mesma pessoa (conferindo nome completo, CRM, UF e município quando disponível).
3. **Etapa C — Extração de Especialidades e RQEs:**
   - No resultado oficial individualizado do CFM/CRM, registrar:
     * Situação do CRM (Ativo / Regular / Cancelado / Transferido);
     * Especialidade(s) e número(s) do RQE;
     * Área(s) de Atuação.
4. **Etapa D — Rastreabilidade:**
   - Registrar claramente a fonte de cada dado na resposta para permitir conferência pelo analista de reembolso.

---

## 3. CHECKLIST PRÉ-RESPOSTA
Antes de emitir a resposta, valide mentalmente:
- O CRM pertence exatamente ao médico pesquisado?
- A UF está correta?
- A especialidade foi confirmada em fonte oficial do CFM/CRM ou é mera alegação de site comercial?
- Área de atuação não foi rotulada indevidamente como especialidade?
- Foram listadas todas as especialidades se o médico tiver múltiplos RQEs?
