# DIRETRIZES DE TÉCNICAS FISIOTERAPÊUTICAS E REGRAS DE "A CONFIRMAR"

Este documento estabelece o protocolo de auditoria e desambiguação quando o pedido médico, guia ou relatório apresentar apenas uma técnica fisioterapêutica isolada ou quando faltarem dados para a confirmação do código definitivo.

---

## 1. PRINCÍPIO DA ESPECIFICIDADE E NÃO-APROXIMAÇÃO
- **Regra Fundamental:** A fisioterapia no padrão TUSS e THSM é estruturada principalmente pela **patologia clínica** ou pelo **segmento anatômico acometido**, e não pelo nome comercial da técnica empregada pelo fisioterapeuta.
- Se o médico solicitar apenas uma técnica (ex: "Fisioterapia motora", "Cinesioterapia", "RPG", "Pilates", "Hidroterapia", "Liberação miofascial", "Terapia manual") sem especificar a patologia, lesão ou região corporal:
  1. **NÃO assumir uma região por dedução;**
  2. **Marcar os 3 primeiros campos da tabela (Código THSM, Código TUSS e Terminologia) como `A CONFIRMAR`;**
  3. No campo **Justificativa**, descrever o enquadramento-base da técnica e apontar com clareza o que impede o fechamento definitivo do código;
  4. No campo **Alerta**, listar objetivamente as variáveis clínicas necessárias no formato padronizado:
     ```text
     [TÉCNICA A CONFIRMAR]<br>• Confirmar diagnóstico clínico / patologia atendida<br>• Confirmar região anatômica tratada (ex.: segmento da coluna ou membros)
     ```

---

## 2. MAPA DE CONDUTA POR TÉCNICA ISOLADA

### 2.1. Cinesioterapia / Fisioterapia Motora Geral (sem patologia/região)
- **Cenário:** Pedido cita apenas "Fisioterapia motora 10 sessões" ou "Cinesioterapia".
- **Conduta:**
  * Código THSM: `A CONFIRMAR`
  * Código TUSS: `A CONFIRMAR`
  * Terminologia: `A CONFIRMAR`
  * Justificativa: Solicitação genérica de fisioterapia motora sem identificação da patologia osteomioarticular ou segmento corporal acometido.
  * Similares relevantes: `TUSS 20103484 — Patologia osteomioarticular em um membro` | `TUSS 20103506 — Patologia em um segmento da coluna`
  * Alerta: `[SEGMENTO A CONFIRMAR]<br>• Confirmar se o tratamento é para membro (unilateral ou bilateral) ou coluna vertebral`

### 2.2. R.P.G. (Reeducação Postural Global)
- **Cenário 1 — Com indicação clínica de alteração postural estrutural:**
  * Se o pedido indicar escoliose, cifose ou hiperlordose estrutural => enquadra em `20103182 | 25060040 — Desvios posturais da coluna vertebral`.
- **Cenário 2 — Com indicação clínica de dor mecânica em segmento da coluna:**
  * Se for lombalgia, cervicalgia ou dorsalgia => enquadra no código do segmento correspondente (`20103506` para 1 segmento ou `20103514` para múltiplos).
- **Cenário 3 — Pedido isolado "RPG 10 sessões" (sem diagnóstico):**
  * Código THSM: `A CONFIRMAR` (ou `25100076` se houver cobertura expressa de tabela para o procedimento específico de RPG)
  * Código TUSS: `A CONFIRMAR` (ou `50000446` para RPG específico)
  * Alerta: `[INDICAÇÃO DO RPG A CONFIRMAR]<br>• Confirmar se a indicação é para desvio postural estrutural ou patologia dolorosa de coluna`

### 2.3. Pilates
- **Regra Contratual e do Rol da ANS:**
  * O método Pilates não integra o Rol de procedimentos de cobertura obrigatória da ANS.
  * Se cobrado exclusivamente como a técnica/método Pilates isolado: não possui cobertura, salvo cláusula contratual específica (ex.: apólices ANBIMA, IBM, Kyndryl).
  * Se houver prescrição de patologia clínica (ex.: reabilitação lombar) e a conduta for cinesioterapia de fortalecimento realizada em estúdio de Pilates sem cobrança de taxa extra: enquadrar pelo código da patologia tratada (`20103506`).
- **Se pedido cita apenas "Pilates clínico":**
  * Código THSM: `A CONFIRMAR`
  * Código TUSS: `A CONFIRMAR`
  * Alerta: `[COBERTURA DE PILATES A CONFIRMAR]<br>• Confirmar diagnóstico clínico e se há cláusula contratual de extensão de cobertura para o método Pilates`

### 2.4. Drenagem Linfática
- **Cenário Clínico / Terapêutico:**
  * Linfedema, lipedema clínico com relatório, insuficiência venosa crônica, pós-operatório com edema patológico ou pós-cirurgia oncológica com dissecção axilar/inguinal => `20103212 | 25030019 — Distúrbios circulatórios artério-venosos e linfáticos`.
- **Cenário Estético:**
  * Redução de medidas, celulite, modelagem corporal ou pós-operatório estético => Não coberto.
- **Se pedido cita apenas "Drenagem linfática":**
  * Alerta: `[INDICAÇÃO CLÍNICA A CONFIRMAR]<br>• Confirmar diagnóstico de base (linfedema/distúrbio circulatório) para descartar finalidade estética`

### 2.5. Hidroterapia / Fisioterapia Aquática
- **Regra:** Hidroterapia é técnica de reabilitação física realizada em meio aquático. Não possui código TUSS isolado no Rol.
- **Conduta:** O procedimento deve ser enquadrado pelo **código da patologia que motivou o tratamento** (ex.: patologia de membro `20103484` ou neurológica `20103425`).
- **Se pedido cita apenas "Hidroterapia 10 sessões":**
  * Código THSM: `A CONFIRMAR`
  * Código TUSS: `A CONFIRMAR`
  * Alerta: `[PATOLOGIA DE BASE A CONFIRMAR]<br>• Confirmar qual patologia física ou neurológica motivou a indicação da fisioterapia aquática`

### 2.6. Agulhamento a Seco (Dry Needling - 20103301) vs Acupuntura (31601014)
- **Conforme Manual Oficial:**
  * **Agulhamento a Seco (20103301 / THSM 16010191):** É ato privativo de **Médico Fisiatra** (CRM). Fisioterapeuta **NÃO** pode realizar agulhamento a seco para fins de reembolso.
  * **Acupuntura Tradicional (31601014 / THSM 25100165):** Fisioterapeuta legalmente habilitado em Acupuntura pode realizar.
- **Se pedido cita "Dry needling realizado por fisioterapeuta":**
  * Sinalizar incompatibilidade profissional no campo Alerta.

### 2.7. Terapia Manual / Liberação Miofascial / Osteopatia
- **Terapia Manual / Liberação Miofascial:** São recursos técnicos aplicados na sessão. Devem ser enquadrados pelo código da patologia física que originou a queixa (ex: cervicalgia = `20103506`).
- **Osteopatia Pediátrica Funcional:**
  * Cólicas do lactente, refluxo funcional, constipação, torcicolo posicional, dificuldades de amamentação => enquadra em `50000160`.
  * Torcicolo congênito verdadeiro => enquadra em `20103506`.
  * Plagiocefalia / assimetria craniana => enquadra em `20103654`.

### 2.8. Eletroestimulação e Biofeedback Perineal
- **Eletroestimulação do assoalho pélvico isolada:** `20203020 | 25100300`.
- **Biofeedback perineal isolado:** `20103646 | 25100270`.
- **Fisioterapia pélvica convencional (Kegel / cinesio sem aparelho):** `20103190 | 25100117`.
- **Se pedido cita "Fisioterapia pélvica + Biofeedback":**
  * Código Principal: `20103646` (Biofeedback)
  * Código Adicional: `Sim — THSM 25100300 / TUSS 20203020 — Eletroestimulação do assoalho pélvico` (se ambas as técnicas forem solicitadas e realizadas).

---

## 3. PADRONIZAÇÃO DO CAMPO "ALERTA"
O campo Alerta deve ser conciso, sem perguntas prolixas, adotando sempre os prefixos em maiúsculas entre colchetes:
- `Sem alerta` (quando tudo estiver confirmado e sem pendências);
- `[PATOLOGIA A CONFIRMAR]<br>• Confirmar diagnóstico clínico motivador do tratamento`;
- `[LATERALIDADE A CONFIRMAR]<br>• Confirmar se o acometimento é unilateral (um membro) ou bilateral (dois membros)`;
- `[SEGMENTO DA COLUNA A CONFIRMAR]<br>• Confirmar se há apenas um segmento afetado ou múltiplos segmentos vertebrais`;
- `[TÉCNICAS A CONFIRMAR]<br>• Confirmar execução de [Técnica A]<br>• Confirmar indicação de [Técnica B]`.
