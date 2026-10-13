# Matriz de Concomitância, Recibos Múltiplos e Regras Antifraude

## 1. Regra Fundamental de Auditoria

* **Presunção de Execução:** Se o prestador relacionou o código ou técnica na nota fiscal / recibo quitado, considera-se que o procedimento foi executado.
* **Critério de Elegibilidade:** O que autoriza a liberação é se o procedimento ou técnica cobrada possui **indicação clínica e solicitação expressa no pedido médico**.

---

## 2. Regras de Concomitância em Recibo Único

Quando diferentes procedimentos forem cobrados no mesmo recibo/nota fiscal referente ao mesmo dia/atendimento:

| Técnicas Cobradas no Mesmo Recibo | Conduta Regulatória Obrigatória |
|---|---|
| **Biofeedback + Eletroestimulação + Fisioterapia Convencional** | Liberar **apenas Biofeedback (20103646) + Eletroestimulação (20203020)**. A fisioterapia convencional é considerada incorporada às técnicas especializadas. |
| **Biofeedback + Fisioterapia Convencional** | Liberar **apenas Biofeedback (20103646)**. |
| **Eletroestimulação + Fisioterapia Convencional** | Liberar **apenas Eletroestimulação (20203020)**. |
| **Biofeedback + Eletroestimulação** | Liberar **ambos os códigos**, desde que ambos estejam explicitamente prescritos pelo médico. |
| **TENS + Fisioterapia Convencional** | Liberar **ambos os códigos** (TENS pelo 31602185 cumprindo a DUT 24 + código da patologia motora tratada). |
| **RPG + Fisioterapia Convencional** | Liberar **ambos os códigos**, desde que a apólice do beneficiário possua cláusula/pacote extra-ROL para RPG. |

---

## 3. Concomitância em Recibos Separados

* **Apresentação de Recibos Distintos:** A cobrança em documentos fiscais separados não invalida a sessão de fisioterapia convencional. Cada documento é analisado individualmente com seus respectivos valores.
* **Tentativa de Fracionamento Abusivo:** Se o prestador emitir recibos separados cobrando 3 ou 4 técnicas na mesma data (ex.: cinesioterapia motora + respiratória + TENS + laser) visando multiplicar valores sem justificativa clínica:
  * Pagar a patologia motora principal;
  * Glosar as técnicas não solicitadas por **`N415`** ou exigir a discriminação documental por **`A170`**.

---

## 4. Cenários de Divergência entre Pedido Médico e Cobrança

### Cenário 1: Cobrança Padrão com Técnica Especial (TENS, RPG, Biofeedback)
1. **Fisio + Técnica com valores discriminados, mas médico NÃO prescreveu a técnica:**
   * Emitir pendência **`A206 A`** (solicitar pedido médico com indicação da técnica).
   * Sem retorno do beneficiário: somar os valores e remunerar apenas pelo código da patologia motora coberta.
2. **Fisio + Técnica sem valores discriminados, e o médico prescreveu ambos:**
   * Emitir pendência **`A170`** (solicitar discriminação do valor cobrado por procedimento/sessão).
3. **Fisio + Técnica sem valores discriminados, e o médico NÃO prescreveu a técnica:**
   * Emitir pendência conjunta **`A170 + A206 A`**.
4. **Cobrou apenas Fisioterapia convencional, mas o médico prescreveu a técnica:**
   * Pagar conforme a cobrança apresentada (pelo código da patologia coberta).

### Cenário 2: Múltiplos Códigos de Fisioterapia na Mesma Sessão
* **Médico prescreveu apenas fisioterapia geral, mas a nota cobra múltiplos códigos:**
  * Somar os valores e pagar sob uma única patologia principal.
* **Cobrança de Cinesioterapia Respiratória junto com Motora:**
  * Somente é permitida a liberação concomitante de código motor (ex.: 20103484) com respiratório (ex.: 20103220) se houver **doença pulmonar ativa comprovada** no laudo (ex.: asma, bronquiectasia, pneumonia ativa). Sem doença respiratória ativa, remunerar apenas o código motor.

---

## 5. Reeducação Postural Global (RPG)

* **Classificação TUSS:** `50000446` | **THSM:** `25100076`.
* **Natureza Regulatória:** Procedimento enquadrado como *"ROL NÃO / DIVULGA SIM"*.
* **Diretriz de Cobertura:**
  * Se a apólice possuir cláusula ou modalidade com cobertura para procedimentos extra-ROL: **liberar o código de RPG**.
  * Se a apólice for estrita ao ROL obrigatório da ANS sem cobertura acessória: **glosar por N205**.
