# DIRETRIZES OFICIAIS DO CFM: ESPECIALIDADES MÉDICAS E RQE

Este documento estabelece as diretrizes regulatórias do Conselho Federal de Medicina (CFM) para identificação, validação e auditoria de especialidades médicas e Registro de Qualificação de Especialista (RQE).

---

## 1. O QUE CONSTITUI "ESPECIALIDADE CONFIRMADA"
- Conforme a Resolução CFM e legislação brasileira, **especialista é exclusivamente o médico que possui Registro de Qualificação de Especialista (RQE)** regularmente inscrito no CRM do Estado onde atua.
- **Não constituem nem provam RQE:**
  * Pós-graduação lato sensu (mesmo reconhecida pelo MEC);
  * Cursos de extensão, aperfeiçoamento ou reciclagem;
  * Fellowships nacionais ou internacionais;
  * Cargos de chefia de serviço ou setores hospitalares;
  * Menções em páginas de terceiros, redes sociais ou Doctoralia ("especialista em coluna", "focado em emagrecimento");
  * Atuação prática habitual declarada pelo próprio profissional.

---

## 2. ESPECIALIDADE VS ÁREA DE ATUAÇÃO
- **Especialidade Médica:** Área troncal reconhecida pela Comissão Mista de Especialidades (CFM/AMB/CNRM), dotada de RQE próprio (ex: Cardiologia, Pediatria, Ortopedia e Traumatologia, Ginecologia e Obstetrícia, Clínica Médica).
- **Área de Atuação:** Qualificação complementar ou derivada vinculada a uma especialidade base (ex: Dor, Ecocardiografia, Medicina do Sono, Endoscopia Ginecológica, Hansenologia).
- **Regra de Auditoria:** Especialidade e Área de Atuação devem ser apresentadas de forma estritamente separada. Nunca classifique uma área de atuação como especialidade.

---

## 3. REGRA DA UNIÃO DE RQEs (MÚLTIPLAS ESPECIALIDADES)
- Médicos podem possuir legitimamente mais de uma especialidade registrada (ex: Clínica Médica e Nefrologia; Cirurgia Geral e Urologia).
- **Regra de Unificação:**
  * Se o portal do CFM individualizado listar mais de uma especialidade, listar TODAS com seus respectivos RQEs.
  * Se o CFM exibir uma especialidade (ex: Cardiologia) e o CRM regional exibir outra especialidade para o mesmo profissional (ex: Clínica Médica), e nenhuma das fontes negar a outra, realize a **UNIÃO** das especialidades confirmadas: `Cardiologia; Clínica Médica`.
  * **Atenção:** Isso **NÃO é divergência**. Divergência real ocorre apenas quando fontes oficiais entram em contradição direta sobre identidade, cancelamento do CRM, fraude cadastral ou negação explícita de um registro.

---

## 4. HIERARQUIA DE EVIDÊNCIA
1. **Fontes Oficiais Primárias (Prevalência Absoluta):**
   - CFM — Busca por Médicos: `https://portal.cfm.org.br/busca-medicos/`
   - Portais dos Conselhos Regionais de Medicina (CREMERJ, CREMESP, CRM-MG, etc.).
2. **Fontes Institucionais Secundárias (Apoio / Desambiguação):**
   - Grandes redes hospitalares (Albert Einstein, Sírio-Libanês, Rede D'Or, HC/USP, hospitais federais);
   - Currículo Lattes (CNPq) para histórico acadêmico.
3. **Diretórios Comerciais (Apenas Descoberta de Pistas):**
   - Doctoralia, CatalogoMed, etc. (Úteis para achar pistas de UF ou homônimos, mas NUNCA suficientes para atestar RQE oficial).

---

## 5. HOMÔNIMOS E PARSER DE ENTRADA
- Se houver múltiplos médicos com o mesmo nome completo, os dados de CRM e UF têm peso absoluto de desempate sobre pequenas divergências de grafia de nome.
- Se o usuário fornecer apenas Nome sem CRM e sem UF, não pesquisar e solicitar:
  `"Por favor, forneça o número do CRM ou o Estado de atuação para que eu possa identificar o médico corretamente."`
- Se fornecer CRM sem UF e o nome for comum:
  `"Por favor, informe a UF do CRM para que eu possa identificar o médico corretamente."`
- Nunca solicitar informações que já constam na mensagem ou documento do usuário.
