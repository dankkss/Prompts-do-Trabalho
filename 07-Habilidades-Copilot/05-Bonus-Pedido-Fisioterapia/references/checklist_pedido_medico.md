# Checklist de Conformidade do Pedido Médico

## 1. Requisitos Obrigatórios de Validação
Ao analisar qualquer prescrição ou pedido médico, verificar:
1. **Identificação do Médico:** Nome completo, CRM e UF de emissão (por carimbo legível, cabeçalho institucional ou assinatura digital com chave pública ICP-Brasil validável).
2. **Identificação do Paciente:** Nome do beneficiário (compatível com a apólice).
3. **Data da Prescrição:** Data legível de emissão; verificar se está dentro da validade aplicável.
4. **Indicação Clínica / Diagnóstico:** Descrição da patologia, quadro clínico ou código CID-10 correspondente.
5. **Procedimento Solicitado:** Discriminação de fisioterapia, quantidade de sessões (se informada) e técnicas específicas pretendidas (ex.: motora, respiratória, TENS, RPG, biofeedback).

## 2. Conduta Operacional em Casos de Irregularidade
* Sem CRM ou médico não identificado -> emitir pendência `A109` ou `A199`.
* Imagem de assinatura colada ou PDF sem validação ITI -> emitir `A198`.
* Pedido rasurado -> emitir `A197 A`.
* Pedido sem data -> emitir `A197`.
* Pedido com validade expirada -> solicitar renovação com emissão que pode ser posterior ao início do tratamento.
