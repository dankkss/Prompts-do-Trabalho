# Manual de Especificidade e Desempate de Críticas de Complemento (A)

Este catálogo contém a inteligência operacional para aplicação precisa das críticas de **COMPLEMENTO (Pendência Documental - A)**.

---

## 1. Princípios e Hierarquia de Escolha

1. **Regra de Ouro da Especificidade:**
   Sempre prefira: **Variante/Subcategoria específica > Crítica-base da família > Crítica genérica > Fallback residual (`A150`)**.
2. **Uso do A150:** `A150` é estritamente o último recurso residual. Nunca utilize `A150` quando existir crítica específica que cubra o documento ou a informação solicitada.
3. **Identificadores Exatos:** Utilize sempre a sigla oficial completa, inclusive o subtipo cadastrado na base (ex.: `A116 - Psicoterapia`, `A109 A - PSICOTERAPIA ESPECIALIDADE PSIQUIATRA`, `A205 D - Assinatura digital não validável de prestador`).
4. **Diferenciação Probatória:**
   Nunca confunda: **AUSENTE** × **INCOMPLETO** × **ILEGÍVEL** × **SEM VALIDADE FISCAL/AUTENTICIDADE COMPROMETIDA**.
   * Se o documento foi enviado mas não se consegue ler: aplicar a variante de ilegibilidade (`A156`), nunca crítica de ausência.
   * Se falta comprovação de assinatura digital: aplicar críticas de validação eletrônica (`A198` ou `A205`), nunca ausência simples.

---

## 2. Desempates Críticos por Família

### A. Atendimentos vs Procedimentos vs Técnicas
* **A103 × A123:**
  * `A103`: Solicita a descrição de quais **atendimentos** foram prestados (consulta, orientação, terapia, curativo).
  * `A123`: Solicita a discriminação de qual **procedimento ou cirurgia** foi executado.
* **A107 × A107 A × A206 A:**
  * `A107`: Solicita qual **técnica** foi executada (cinesioterapia, eletroterapia, terapia manual).
  * `A107 A`: Solicita **técnica + região corporal tratada** (necessária para codificação fisioterapêutica).
  * `A206 A`: O prestador cobrou uma técnica específica, mas ela **não foi solicitada pelo médico** no pedido.
  * *Regra de Desempate:* Se falta execução técnica -> `A107/A107 A`. Se falta pedido médico para a técnica cobrada -> `A206 A`.

### B. Especialidades e Qualificação Médica
* **A109:** Solicita a especialidade médica genérica quando ausente no atendimento.
* **A109 A - PSICOTERAPIA ESPECIALIDADE PSIQUIATRA:**
  * Uso restrito para **psicoterapia realizada por médico** sem qualificação comprovada em Psiquiatria.
  * Solicita formalmente: Certificado de Residência Médica em Psiquiatria e/ou Título de Especialista em Psiquiatria.
  * **Atenção:** Nunca aplicar `A109 A` para psicólogo; psicoterapia por psicólogo exige apenas CRP ativo.

### C. Documentos Fiscais, Recibos e Quitação
* **A110:** Documento sem validade fiscal adequada (recibo sem quitação, documento provisório; não dizer "sem valor monetário").
* **A110 A:** Nome do paciente divergente ou fora do contrato/apólice.
* **A110 B:** Comprovante de pagamento de parcela de tratamento (exigir a quitação do valor total cobrado).
* **A157 (Recibo de Papelaria):** Recibo avulso sem identificação de clínica/consultório; solicita comprovação do local, endereço, telefone e ambiente do atendimento.
* **A157 A:** Solicita exclusivamente a comprovação do ambiente de atendimento.
* **A213:** Documento fiscal contém datas futuras ou serviços ainda não realizados.

### D. Assinaturas Digitais e Fraude Documental
* **A198:** Pedido médico ou relatório emitido por **MÉDICO (CRM)** contendo colagem de assinatura ou assinatura digital que não valida nos padrões oficiais (ITI / ICP-Brasil / CFM).
* **A205 C:** Relatório emitido por **PRESTADOR NÃO-MÉDICO** (fisioterapeuta, psicólogo, fonoaudiólogo) contendo colagem de imagem de assinatura.
* **A205 D:** Assinatura digital de **PRESTADOR NÃO-MÉDICO** que não valida nos padrões oficiais (ITI / ICP-Brasil).
* **A205 A:** Documento **FISCAL** (NFS-e/recibo) com colagem de assinatura.
* **A205 B:** Assinatura eletrônica de documento **FISCAL** não validável.
* **Regra de Ouro:** Se o documento for de médico CRM -> usar estritamente `A198`. Se for de outro profissional de saúde -> usar `A205 C/D`.

### E. Comprovantes de Desembolso Financeiro
* **A188:** Solicitação geral de comprovante de desembolso financeiro (TED, DOC, PIX, extrato bancário).
* **A188 A:** Pagamento informado em espécie (dinheiro vivo); exige carta de próprio punho explicando a origem dos recursos e quitação.
* **A188 B:** Comprovante bancário apresentado possui valor inferior ao valor do recibo/nota fiscal.
* **A188 C:** Comprovante apresentado refere-se a mero agendamento bancário sem efetivação da transação.
* **A189 (Uso Restrito Antifraude):**
  * Aplicar **somente** quando coexistirem: ausência de comprovação de desembolso + suspeita fundamentada de fraude/abuso + valor igual ou superior a R$ 10.000,00. Solicita cópia de RG, CPF e comprovante de residência do segurado.

### F. Terapias Multidisciplinares e Exames
* **A114:** Uso exclusivo para **EXAMES** complementares (falta nome técnico ou indicação clínica). Não usar para terapias!
* **A116 (Terapias):** Utilizar sempre o subtipo da profissão:
  * `A116 - Acupuntura` | `A116 - Fisioterapia` | `A116 - Fonoaudiologia` | `A116 - Nutricionista` | `A116 - Psicoterapia` | `A116 - Terapia ocupacional`.
  * `A116 A`: Já existe documentação, mas falta quadro clínico e diagnóstico detalhado.
* **A200:** Solicita relatório de plano de tratamento multidisciplinar.
* **A200 A:** Solicita ficha de frequência com datas e assinaturas das sessões de terapias.

### G. Faturas Hospitalares e Prontuários
* **A125 - Conta Hospitalar:** Fatura hospitalar sem discriminação de itens (diárias, taxas, medicamentos).
* **A125 - Pacote:** Fatura cobrada sob regime de pacote sem detalhamento dos serviços incluídos.
* **A209:** Faltam páginas da fatura hospitalar.
* **A209 A:** Faltam páginas do prontuário médico.
