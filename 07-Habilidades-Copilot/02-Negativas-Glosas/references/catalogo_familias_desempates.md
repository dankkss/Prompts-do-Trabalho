# Catálogo Unificado de Negativas (Glosas), Famílias e Regras de Desempate

Este catálogo unifica a inteligência regulatória para contratos **Pós-Lei (TUSS / Rol ANS)** e **Pré-Lei (THSM / MPAS / Contratual)**.

---

## 1. Princípio de Precedência e Hierarquia
A escolha da negativa operacional correta segue estritamente a ordem:
**Pré-requisito formal > Variante / Cenário específico > Família da glosa > Genérica > Fallback (N305)**.

* Regra de Especificidade: Uma negativa específica de diretriz (Rol/DUT/RN) sempre prevalece sobre as genéricas `N205`, `N221`, `N293` e `N294`.
* **Proibição Absoluta:** As críticas **N406** e **N369** estão formalmente DESATIVADAS na base ativa. Nunca utilizá-las como recomendada, alternativa, similar ou fallback. Se apenas elas parecerem aplicáveis, declare: `NEGATIVA NÃO IDENTIFICADA NA BASE ATIVA`.
* **Fallback N305:** O código `N305` é estritamente o último recurso residual quando nenhuma negativa específica ou genérica atender ao cenário.

---

## 2. Diferenciação por Regime Contratual (Pós-Lei vs Pré-Lei)

### Exclusivas de Pós-Lei (Lei 9.656/98 / TUSS / Rol da ANS):
* `N205`: Despesa sem cobertura prevista no Rol de Procedimentos da ANS.
* `N293`: Exame realizado fora das Diretrizes de Utilização (DUT) da ANS.
* `N294`: Procedimento / Cirurgia realizada fora das Diretrizes de Utilização (DUT) da ANS.
* `N306 (Pós)`: Procedimento executado por profissional não previsto na TUSS.
* `N432`: Ultrassonografia para controle de ovulação que excedeu o limite da DUT.

### Exclusivas de Pré-Lei (Contratos Antigos / THSM / MPAS):
* `N306 (Pré)`: Profissional executante fora da Tabela THSM.
* `N336`: Procedimento não constante da Tabela THSM.
* `N318 / N280`: Profissional ou procedimento fora da Tabela MPAS.
* `N247 / N248 / N320`: Cirurgias refrativas em apólices pré-lei.

### Transversais (Válidas em Ambos os Regimes):
* `N210`: Curativos em ambulatório sem previsão contratual.
* `N309`: Atendimento pós-operatório realizado dentro de 10 dias do ato cirúrgico (já incluso no porte anestésico/cirúrgico).
* `N425` a `N431`: Parcelamentos, reembolsos em duplicidade, procedimentos cobrados diferentes dos executados e Receita Saúde.

---

## 3. Pré-Requisitos Rígidos e Desempates Críticos

* **Reanálise:**
  * `N298`: O valor pago anteriormente estava correto (reanálise mantida com pagamento confirmado).
  * `N298A`: A negativa anterior foi reanalisada e mantida integralmente.
* **CNES e Estabelecimento:**
  * `N368`: Ausência de cadastro do CNES apurada e confirmada manualmente.
  * `N387`: Irregularidade de CNES apontada automaticamente pela ferramenta CRIVO.
* **Conselhos Profissionais:**
  * `N378`: Irregularidade cadastral apontada pela ferramenta CRIVO.
  * `N424`: Irregularidade cadastral no Conselho apurada manualmente (quando o CRIVO não trouxe retorno).
* **Fracionamento de Recibos:**
  * `N375`: Exige indício claro de divisão artificial da mesma sessão. Não aplicar se os documentos representam atendimentos de datas ou especialidades comprovadamente distintas.
  * `N375B`: Bloqueio automático de LPL sistêmico.
* **Desembolso e Pagamento:**
  * `N390`: Comprovante de desembolso financeiro já solicitado previamente por complemento e não enviado pelo beneficiário.
  * `N421`: Documento ou transação bancária existe, mas não comprova desembolso efetivo (houve estorno, repasse ou devolução de valores).
* **Junta Médica:**
  * `N417`: Negativa integral após emissão de parecer conclusivo de Junta Médica.
  * `N417A`: Negativa parcial após parecer de Junta Médica.
* **Auditoria Antifraude:**
  * `N429`: Exige parecer prévio da Auditoria comprovando que o procedimento cobrado foi diferente do efetivamente executado.
  * `N430`: Receita Saúde inexistente na base da Receita Federal.
  * `N430A`: Receita Saúde cancelada pelo prestador.
* **Fisioterapia e Técnicas:**
  * `N373`: Ausência total de pedido médico ou odontológico.
  * `N415`: Fisioterapia motora foi solicitada, mas a técnica específica cobrada (ex.: TENS ou laser) não consta na prescrição.
  * `N416`: Biofeedback (20103646) cobrado fora de indicação perineal/uroginecológica (nunca aplicar para o biofeedback EMG 20103131).
  * `N433`: Fisioterapia voltada a transtornos mentais/psíquicos (não coberta; fisioterapia cobre apenas reabilitação física).
  * `N226`: Reabilitação/fisioterapia executada por profissional não habilitado (substitui a histórica N349).
* **Vacinas:**
  * `N290`: Vacina sem cobertura por estar fora das Condições Particulares (CP) ou aditivo (crítica 290 CP).

---

## 4. Famílias de Similaridade Obrigatórias

Sempre que a negativa pertencer a uma das famílias abaixo, a resposta deve listar **TODOS os demais membros ativos da família**, apontando resumidamente a diferença de cada um:

1. **Documento Repetido:** `N285`, `N285A`, `N285B`, `N285C`.
2. **Reanálise:** `N298`, `N298A`, `N300`, `N301`, `N307`, `N308`, `N337`.
3. **CNES:** `N368`, `N387`.
4. **Conselho de Classe:** `N378`, `N424`.
5. **Fracionamento:** `N375`, `N375B`.
6. **Desembolso Financeiro:** `N376`, `N390`, `N421`.
7. **Receita Saúde:** `N430`, `N430A`.
8. **Ressarcimento:** `N501`, `N501-OPERADORA`.
9. **Junta Médica:** `N417`, `N417A`.
10. **Reembolso Específico:** `N407` (consultas/terapias por não médicos sob AHO), `N408` (HM internação), `N409` (outra despesa sem previsão), `N410` (HO fora pré-natal).
11. **Rol / DUT Genéricas:** `N205`, `N221`, `N293`, `N294`.
12. **Enfermagem:** `N358`, `N358A`.
13. **Fisioterapia / Indicação:** `N373`, `N415`, `N416`, `N433`.
14. **Ostomia:** `N324`, `N426`, `N426A`, `N426B`.
15. **Odontologia:** `N331`, `N331A`, `N332`, `N367`, `N360`.
16. **Teleatendimento:** `N353`, `N354`, `N418`.
17. **Reembolso Duplicado:** `N427`, `N428`.
18. **Testes de Farmácia:** `N365` (Covid), `N366` (Influenza), `N412` (Dengue).
