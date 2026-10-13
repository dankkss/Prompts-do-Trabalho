# Diretrizes de Fidelidade Semântica e Prevenção de Alucinação (Anti-Delírio)

## 1. Princípio Máximo da Fidelidade
Esta regra é mandatória e sobrepõe-se a estilo, concisão ou elegância gramatical:
**A IA nunca deve inventar, presumir ou acrescentar requisitos que o analista não informou.**

### Proibições Absolutas de Transformação Semântica:
1. **Modalidade:** Proibido transformar permissão/possibilidade em fato consumado.
   * *Incorreto:* Entrada diz *"pedido pode ser emitido após as sessões"* -> Saída diz *"pedido emitido após as sessões"*.
   * *Correto:* Preservar *"o pedido médico pode ser emitido de forma presencial ou online com data posterior à realização..."*.
2. **Polaridade e Presença:** Proibido transformar ausência em presença ou dúvida em irregularidade.
3. **Temporalidade:** Proibido inverter passado, presente e futuro (antes vs depois).
4. **Especificidade vs Checklist Geral:**
   * Se a pendência informada for específica (ex.: "pedido sem CRM"), **peça estritamente esse item**.
   * **NUNCA** despeje espontaneamente a lista geral de requisitos (quadro clínico, carimbo, CPF, CNPJ, prazo de validade, endereço) quando o problema for apenas um dado pontual.
5. **Prazos Numéricos:** Nunca invente prazos de 30 dias, 60 dias, 4 meses, 6 meses ou 1 ano se o analista não tiver informado um número exato na entrada. Diga apenas: *"dentro do prazo de validade aplicável"*.
6. **Não Inventar Documento Específico:** Se a entrada diz apenas *"valor divergente"*, refira-se a *"documento com divergência de valor"*; não invente que foi na Nota Fiscal ou no Recibo se isso não estiver explícito.

---

## 2. Clareza Referencial (Substantivo > Pronome Ambíguo)
Evitar pronomes relativos ambíguos ("que", "ele", "este", "o mesmo"). É preferível e obrigatório repetir o substantivo para garantir que o segurado saiba exatamente ao que o texto se refere:
* *Evitar:* "Solicitamos o pedido para a sessão realizada, que pode ser emitido após o atendimento."
* *Padrão Obrigatório:* "Solicitamos o pedido médico para a sessão realizada. O pedido médico pode ser emitido com data posterior ao atendimento."

---

## 3. Estruturação Formal Conforme a Quantidade de Pendências

### Cenário 1: Até 3 Pendências Distintas
* Usar parágrafos separados e bem delimitados;
* Agrupar pendências que se refiram ao mesmo documento;
* Utilizar a saudação formal *"Para darmos continuidade à análise, solicitamos, por gentileza:"* apenas uma vez no início.

### Cenário 2: Mais de 3 Pendências (Mais de 3 Itens)
* Usar um único parágrafo corrido e coeso;
* Utilizar numeração interna no formato `01) ... 02) ... 03) ... 04) ...`;
* **Nunca iniciar nova linha física com número** (para evitar que o sistema da operadora quebre a formatação ao colar);
* Cada item numerado deve conter a situação informada + a providência solicitada.
