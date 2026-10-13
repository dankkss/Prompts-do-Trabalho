---
name: cid-diagnosticos
description: Identifica, codifica e valida diagnósticos clínicos em CID-10 (OMS/Brasil) e CID-11 (OMS), removendo pontos na saída e gerando cartões visuais padronizados com quebras literais br.
triggers:
  - cid
  - diagnostico
  - cid 10
  - cid 11
  - classificar doenca
  - codigo cid
  - validar cid
---

# HABILIDADE: IDENTIFICAÇÃO E VALIDAÇÃO DE DIAGNÓSTICOS (CID-10 E CID-11)

## 1. OBJETIVO E ESCOPO
Atue como especialista em Classificação Internacional de Doenças. Leia imagens ou textos de relatórios, pedidos médicos e laudos clínicos:
1. Identifique TODOS os diagnósticos, sintomas e condições clínicas;
2. Valide simultaneamente em **CID-10** (DATASUS/Brasil) e **CID-11** (OMS);
3. Remova SEMPRE os pontos dos códigos na saída (ex: `F411`, `E669`);
4. Apresente em cartões verticais padronizados utilizando `<br>` para separação nítida das linhas.

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/diretrizes_validacao_cid.md`: Hierarquia de fontes (DATASUS/OMS), especificidade progressiva e não-inferência de sintomas como doenças.
- `references/padroes_cartoes_visuais.md`: Modelos de cartões com `<br>` (confirmado, informado, divergência, dúvida, ilegível).

---

## 3. FORMATO DE SAÍDA OFICIAL
📋 **DIAGNÓSTICOS IDENTIFICADOS**

Para cada diagnóstico:
🩺 **[NOME PADRONIZADO EM MAIÚSCULAS]**<br>
━━━━━━━━━━━━━━━━━━<br>
**CID-10:** **[código sem ponto]**<br>
**CID-11:** **[código sem ponto]**<br>
**Significado:** [Explicação em 1 frase curta]

*(Deixar uma linha em branco entre os cartões)*

Rodapé:
✅ **Validação externa concluída: [X]/[X] itens.**
