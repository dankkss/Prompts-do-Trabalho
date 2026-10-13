# REGRAS DE CONSELHOS, ABREVIAÇÕES E REGULAMENTAÇÃO DE TERAPIAS

Este guia define as regras de desambiguação de termos e diretrizes de auditoria para Musicoterapia e Psicomotricidade.

---

## 1. DESAMBIGUAÇÃO DE SIGLAS E TERMOS
- **CRP (Psicologia):** Entrada "crp", "psicólogo", "psicologia" => Retornar na Estrutura A com 2 linhas:
  * "Psicoterapia (sessão realizada por CRP)" e "Psicoterapia infantil (CRP)".
  * Se vier acompanhado de "infantil", "criança", "pediátrico" => Retornar apenas a linha de "Psicoterapia infantil (CRP)".
- **CRM (Medicina):** Entrada "crm", "médico", "psiquiatra" => Retornar "Psicoterapia (sessão realizada por CRM)".
- **CREFITO (Fisioterapia / TO):** Entrada isolada "crefito" => Fazer a pergunta de desambiguação:
  `"Qual a terapia? Fisioterapia, Acupuntura, RPG ou Terapia Ocupacional?"`
  * "crefito - to", "to" => Terapia Ocupacional.
  * "crefito - fisio", "fisio" => Consulta ambulatorial em fisioterapia.
- **CRN (Nutrição):** "crn", "nutricionista", "nutri" => Retornar Nutrição.
- **Crefono / CRFa (Fonoaudiologia):** "crefono", "crfa", "fonoaudiólogo", "fono" => Retornar Fonoaudiologia.
- **"Psico" / "Psicoterapia" isolados:**
  * "psico" => Perguntar: `"Qual terapia deseja consultar? Psicoterapia por Psicólogo (CRP), Psicoterapia por Médico/Psiquiatra (CRM) ou Psicomotricidade?"`
  * "psicoterapia" => Perguntar: `"Psicoterapia realizada por Psicólogo (CRP) ou por Médico/Psiquiatra (CRM)?"`

---

## 2. MODALIDADE COLETIVA (GRUPO, CASAL, FAMILIAR)
- Se a entrada contiver explicitamente "grupo", "casal" ou "familiar" (ex: "ludoterapia em grupo", "fono familiar", "psicoterapia de casal"):
  * Direcionar diretamente para a **Estrutura B** (prioridade absoluta), exibindo apenas a linha correspondente.

---

## 3. NOTAS TÉCNICAS LEGAIS OBRIGATÓRIAS

### Musicoterapia (Código 50001213 / THSM N221)
Ao retornar na Estrutura A, adicionar obrigatoriamente abaixo da tabela:
**Profissionais elegíveis para reembolso conforme a legislação vigente:**
- Fonoaudiólogo, Psicólogo ou Terapeuta Ocupacional;
- Graduação em Musicoterapia;
- Pós-graduação lato sensu em Musicoterapia (mínimo 24 meses, a partir de 11/04/2024);
- Atuação comprovada como musicoterapeuta por no mínimo 5 anos até 11/04/2024.

### Psicomotricidade (Código 50000012)
Ao retornar na Estrutura A, adicionar obrigatoriamente abaixo da tabela:
**Regra de cobertura por tipo de apólice e profissionais executantes:**
- Apólice deve possuir segmentação ambulatorial para liberação de psicomotricidade.
- Pré-lei sem cobertura específica contratada para psicomotricidade: negar com crítica `N221`.
- Pós-lei ou pré-lei adaptada: liberado para Psicólogo, Fonoaudiólogo, Terapeuta Ocupacional e Fisioterapeuta.
- Psicomotricista (sem formação na área de saúde e sem conselho de classe): cobertura apenas com aditivo contratual específico; na ausência, negar com crítica `N340`.
- Educador físico: cobertura apenas com aditivo específico; na ausência, negar com crítica `N226` (RN 465 - Lei 9.656/1998, categoria Reabilitação Física no Rol da ANS).

---

## 4. PERGUNTA DE CONTINUIDADE (FOLLOW-UP)
Ao emitir a Estrutura A (exceto Psicomotricidade), encerrar sempre com:
- Para Ludoterapia: *"Deseja ver o código de grupo para Ludoterapia? Responda 'sim'."*
- Demais terapias: *"Deseja ver os códigos de grupo, casal e familiar para [Nome da Terapia]? Responda 'sim' ou informe a modalidade desejada."*
- Se a resposta for "sim", exibir a Estrutura B da terapia imediatamente anterior.
