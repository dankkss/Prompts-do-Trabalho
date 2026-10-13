# DIRETRIZES DE VALIDAÇÃO DE DIAGNÓSTICOS (CID-10 E CID-11)

Este guia estabelece os parâmetros de codificação clínica, hierarquia de busca oficial e regras de especificidade para auditoria de saúde.

---

## 1. DUPLA CLASSIFICAÇÃO OBRIGATÓRIA (CID-10 E CID-11)
- Todo diagnóstico identificado deve ser validado simultaneamente nas duas classificações:
  * **CID-10:** Classificação Estatística Internacional de Doenças (OMS / Versão DATASUS Brasil).
  * **CID-11:** Classificação Internacional de Doenças 11ª Revisão (OMS).
- **Regra de Remoção de Pontos:** Na saída final, remover SEMPRE os pontos dos códigos para facilitar cópia e colagem no sistema de regulação:
  * `F41.1` => `F411`
  * `E66.9` => `E669`
  * `M54.5` => `M545`
  * `F84.0` => `F840`

---

## 2. HIERARQUIA DE FONTES OFICIAIS
- **CID-10 (Prioridade):**
  1. DATASUS / Ministério da Saúde / Fonte oficial brasileira;
  2. WHO / OMS ICD-10 Browser;
  3. Órgãos públicos e conselhos de saúde.
- **CID-11 (Prioridade):**
  1. WHO / OMS ICD-11 Browser / Coding Tool oficial;
  2. WHO Mapping Tables / Crosswalks oficiais.

---

## 3. ESPECIFICIDADE PROGRESSIVA E NÃO-INFERÊNCIA
- **Especificidade Progressiva:** Utilize o código mais específico que seja diretamente sustentado pelo documento.
  * Se o diagnóstico indicar claramente uma família (ex: "transtorno de ansiedade"), mas não trouxer o subtipo, NÃO deixar como `A CONFIRMAR` por falta de subtipo: busque o código oficial "não especificado" daquela família (ex: `F419`).
- **Sintoma NÃO vira Doença:**
  * Cefaleia não vira enxaqueca;
  * Dor articular não vira artrose;
  * Lombalgia não vira hérnia de disco.
- **Não inferir dados ausentes:** Não adicionar lateralidade (direito/esquerdo), etiologia ou gravidade que não estejam escritas pelo médico.
- **Suspeitas:** Termos como "suspeita de", "a esclarecer" ou "provável" não devem ser codificados como diagnósticos definitivos sem a ressalva clínica.
