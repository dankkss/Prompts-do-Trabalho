# REGRAS ESPECIAIS DE FATURAMENTO E CODIFICAÇÃO TUSS

Este documento orienta o desempate técnico e a auditoria em casos com particularidades de codificação no padrão TUSS da ANS.

---

## 1. REGRA DO DOPPLER (ULTRASSONOGRAFIA)
1. **Verificação Prévia Obrigatória:** Sempre verifique se o procedimento base já inclui o Doppler colorido em sua descrição oficial.
   - *Exemplo:* Código `40901246` (Ultrassonografia de carótidas e vertebrais com Doppler colorido) já embute a tecnologia Doppler. Não adicionar código extra.
   - *Exemplo:* Código `40901262` (Ultrassonografia de tireoide com Doppler colorido) já embute Doppler.
2. **Quando Adicionar Código Suplementar:**
   - Se o exame base NÃO tiver Doppler no descritivo oficial e o pedido médico solicitar estudo com Doppler:
     * Para **Doppler Colorido**: adicionar o código complementar `40901386`.
     * Para **Doppler Pulsado / Espectral / Não especificado**: adicionar o código complementar `40901548`.
   - **Alerta Obrigatório na Saída:**
     ```text
     ATENÇÃO — DOIS CÓDIGOS NECESSÁRIOS:
     - Procedimento base: [código base]
     - Doppler complementar: [40901386 ou 40901548]
     ```

---

## 2. MÚLTIPLAS REGIÕES ANATÔMICAS
- Quando o mesmo método propedêutico (ex: Radiografia, Tomografia Computadorizada, Ressonância Magnética, Ultrassonografia articular) for realizado em topografias distintas:
  * Devem ser lançados códigos separados para cada região, exceto se houver código combinado oficial na TUSS (ex: TC de Abdome Total `41001079`, que engloba abdome superior e pelve).
  * Exemplo: RM de Joelho Direito + RM de Ombro Esquerdo => dois códigos `41101120` (um para cada articulação).

---

## 3. ELETRONEUROMIOGRAFIA (ENMG)
- O código de Eletroneuromiografia (`40103136`) é um ato médico integrado.
- Ele já contempla:
  1. Eletromiografia convencional de agulha;
  2. Testes de velocidade de condução nervosa motora e sensitiva;
  3. Testes de estimulação repetitiva.
- **Regra de Auditoria:** Se a fatura ou pedido apresentar cobrança fracionada desses três componentes, deve ser glosada a fragmentação e mantido apenas o código global da ENMG.

---

## 4. CINTILOGRAFIA DO MIOCÁRDIO E TESTE ERGOMÉTRICO
- O código `40701042` (Cintilografia de perfusão miocárdica em repouso e estresse) **NÃO inclui** os honorários e a execução do teste de esforço físico ou farmacológico.
- **Regra:** Se ambos forem realizados e solicitados:
  * Procedimento de imagem: `40701042` (Cintilografia de perfusão miocárdica);
  * Teste ergométrico de esforço: `40101045` (Teste ergométrico computadorizado).
  * Devem constar como códigos independentes na fatura.

---

## 5. EXAMES ANATOMOPATOLÓGICOS (BIÓPSIAS)
- A denominação genérica "Biópsia" ou "Exame Anatomopatológico" não sustenta um código único. O código correto depende da complexidade do espécime:
  * **Peça simples / biópsia única:** `40601111` (Procedimento diagnóstico em biópsia simples);
  * **Fragmentos múltiplos (ex: biópsia de próstata 12 fragmentos, biópsias gástricas seriadas):** `40601120` (Procedimento diagnóstico em fragmentos múltiplos);
  * **Peça cirúrgica complexa / oncológica com margens cirúrgicas e dissecção linfonodal:** `40601138` (Procedimento diagnóstico em peça cirúrgica complexa).
- Se a requisição ou nota contiver apenas "Biópsia", marcar como **AMBÍGUO** e solicitar o tipo de peça e número de fragmentos.

---

## 6. PRESCRIÇÃO MÉDICA VS NOTA FISCAL (REGRA DE EXECUÇÃO)
- **Princípio Regulatório:** Se o prestador inseriu o código ou descrição do procedimento no recibo ou nota fiscal, presume-se tecnicamente que o ato foi praticado.
- **Critério Decisório de Auditoria:** O fator determinante para liberação ou glosa é se o procedimento foi expressamente solicitado pelo médico assistente no pedido médico. Procedimentos executados pelo prestador sem requisição médica correspondente são passíveis de glosa.
