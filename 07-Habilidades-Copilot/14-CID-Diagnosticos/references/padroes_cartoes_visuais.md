# PADRÕES DE CARTÕES VISUAIS E FORMATAÇÃO COM QUEBRA DE LINHA (<BR>)

Este documento define a sintaxe visual e a regra de renderização dos cartões verticais de diagnósticos para leitura móvel e desktop.

---

## 1. REGRA CRÍTICA DE RENDERIZAÇÃO
Para garantir que os cartões não sofram quebras artificiais de linha em dispositivos móveis, utilize **obrigatoriamente `<br>` literal** entre o título, a linha divisória, os códigos e a descrição.

---

## 2. MODELOS DE CARTÕES

### Modelo 1: Diagnóstico Confirmado Padrão
🩺 **[NOME PADRONIZADO EM MAIÚSCULAS]**<br>
━━━━━━━━━━━━━━━━━━<br>
**CID-10:** **[código sem ponto]**<br>
**CID-11:** **[código sem ponto]**<br>
**Significado:** [Explicação em 1 frase curta, máximo 2]

*(Deixar 1 linha em branco entre cada cartão)*

---

### Modelo 2: Com CID-10 Já Informado no Documento
🩺 **[NOME PADRONIZADO EM MAIÚSCULAS]**<br>
━━━━━━━━━━━━━━━━━━<br>
**CID-10 informado:** **[código sem ponto]** ✅<br>
**CID-11 correspondente:** **[código sem ponto]**<br>
**Significado:** [1 frase curta]

---

### Modelo 3: Caso com Dúvida Clínica / Ambiguidade
⚠️ **[NOME/TERMO EM MAIÚSCULAS]**<br>
━━━━━━━━━━━━━━━━━━<br>
**CID-10:** **[código ou A CONFIRMAR]**<br>
**CID-11:** **[código ou A CONFIRMAR]**<br>
**Significado:** [O que pode ser afirmado com segurança clínica]<br>
**Falta:** [Somente o dado específico necessário para fechar]

---

### Modelo 4: Divergência entre Código Escrito e Diagnóstico
❌ **DIVERGÊNCIA — [NOME/TERMO EM MAIÚSCULAS]**<br>
━━━━━━━━━━━━━━━━━━<br>
**Código informado:** **[código]**<br>
**CID-10 validado:** **[código ou A CONFIRMAR]**<br>
**CID-11 validado:** **[código ou A CONFIRMAR]**<br>
**Problema:** [1 frase objetiva explicando a discrepância clínica]

---

### Modelo 5: Trecho Ilegível
❓ **NÃO IDENTIFICADO**<br>
━━━━━━━━━━━━━━━━━━<br>
**Motivo:** [Breve indicação do trecho ilegível ou rasurado]

---

## 3. RODAPÉ DE AUDITORIA
- Se tudo confirmado:
  ✅ **Validação externa concluída: [X]/[X] itens.**
- Se houver pendências:
  ⚠️ **Validação: [X] confirmados · [Y] a confirmar · [Z] divergências.**
