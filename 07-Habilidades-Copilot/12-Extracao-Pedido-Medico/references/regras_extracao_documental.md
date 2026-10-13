# REGRAS DE EXTRAÇÃO DOCUMENTAL DE PEDIDOS MÉDICOS

Este guia estabelece os parâmetros e padrões rigorosos para a extração de dados clínicos e cadastrais em auditoria de pedidos médicos e requisições de exames/terapias.

---

## 1. CAMPOS OBRIGATÓRIOS E ORDEM DE EXTRAÇÃO
A tabela de saída deve seguir rigorosamente a sequência de campos abaixo:

1. **Nome do Paciente:** Nome completo do paciente. Se ausente, preencher `"não encontrou"`.
2. **Data de Emissão:** Data exata em que o médico emitiu e assinou a prescrição (formato obrigatório `DD/MM/AAAA`).
   * *Atenção:* Não capturar data de validade, data de agendamento ou carimbo de recepção da clínica.
   * Se ausente, preencher `"não encontrou"`.
3. **Sessões:** Extrair APENAS se o documento indicar quantidade exata e total de sessões prescritas (numérica ou por extenso, ex: "10 sessões", "doze sessões" => converter para numeral `12 sessões`).
   * *Regra de Periodicidade:* Menções a frequência (ex: "2 vezes por semana durante 3 meses", "3x/sem") NÃO contam como quantidade exata total. Nesses casos, preencher obrigatoriamente: `"Sem limite de sessões definido no pedido médico"`.
4. **Diagnósticos / CIDs:**
   * Formato obrigatório: **SEM PONTO** separando letra e números (ex: `F840`, `M545`, `E669`).
   * Se houver Diagnóstico e CID no papel: informar ambos.
   * Se houver múltiplos CIDs, listar todos separados por ponto e vírgula (`;`).
   * Se houver apenas o diagnóstico sem o código: identificar o CID-10 correspondente e adicionar a anotação: `"(Identificado pelo assistente AI - não consta no pedido)"`.
   * Se não houver nenhum dos dois: `"não encontrou"`.
5. **Tratamento / Conduta:** Expandir obrigatoriamente abreviações e siglas para o nome por extenso:
   * "Fisio" => `Fisioterapia`
   * "TO" => `Terapia Ocupacional`
   * "RPG" => `Reeducação Postural Global`
   * "Psico" => `Psicologia`
   * "Fono" => `Fonoaudiologia`
6. **Médico Solicitante:** Nome do profissional médico que emitiu o pedido.
7. **Profissional Executante:** Nome do terapeuta ou executante se houver menção explícita na requisição. Caso não conste, preencher `"não se aplica"`.
8. **Registro Profissional:** Número e sigla do Conselho (ex: `CRM-SP 123456`, `CREFITO-3 12345-F`). Se ausente, `"não encontrou"`.
9. **Trecho do Documento:** Transcrever apenas a frase/trecho clínico essencial da conduta médica recomendada.

---

## 2. INDICAÇÃO DE CONFIANÇA NA LEITURA (OCR)
- Palavra ou número com leitura parcialmente incerta: registrar a leitura mais provável seguida de `(provável)`.
- Trecho completamente ilegível: registrar `[ilegível]`.

---

## 3. BLINDAGEM DE DADOS SENSÍVEIS (PRIVACIDADE ZERO-LEAK)
- Omitir estritamente: CPF, RG, número de telefone, endereço residencial e dados de pagamento.
- Manter apenas nome do paciente e dos profissionais envolvidos.

---

## 4. MÚLTIPLAS IMAGENS / DOCUMENTOS
- Se as imagens forem páginas contínuas do mesmo pedido (mesmo paciente e data), consolidar todas as informações em uma única tabela.
- Se forem pedidos médicos diferentes (datas distintas ou pacientes diferentes), emitir tabelas verticais separadas identificadas por cabeçalho simples (ex: `### Pedido Médico 1`, `### Pedido Médico 2`).
