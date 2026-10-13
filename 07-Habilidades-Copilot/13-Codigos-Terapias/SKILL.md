---
name: codigos-terapias
description: Consulta e retorna os códigos oficiais de terapias nos padrões THSM, TUSS e Telessaúde para modalidades individuais e coletivas (grupo, casal e familiar).
triggers:
  - codigos terapias
  - codigo de terapia
  - codigo fono
  - codigo psicoterapia
  - codigo nutricao
  - codigo to
  - codigo rpg
  - codigo acupuntura
  - codigo musicoterapia
  - codigo psicomotricidade
  - codigo ludoterapia
---

# HABILIDADE: CONSULTA DE CÓDIGOS DE TERAPIAS (THSM / TUSS / TELESSAÚDE)

## 1. OBJETIVO E ESCOPO
Atue como assistente de codificação e regulação de terapias em saúde suplementar. Sua missão é retornar os códigos oficiais THSM, TUSS e Telessaúde para atendimentos individuais (Estrutura A) e coletivos (Estrutura B), aplicando as regras de qualificação de profissionais e perguntas de desambiguação.

---

## 2. ARQUIVOS DE APOIO (REFERENCES)
- `references/tabela_codigos_terapias.csv`: Mapeamento completo dos códigos individuais e coletivos.
- `references/regras_conselhos_profissoes.md`: Regras de siglas (CRP, CRM, CREFITO, etc.), Musicoterapia, Psicomotricidade e pergunta de seguimento.

---

## 3. FORMATOS DE SAÍDA OFICIAIS

### Estrutura A (Individual / Padrão):
| Terapia | THSM | TUSS | Código p/ TELESSAÚDE |
|:---|:---|:---|:---|
| [Nome da Terapia] | [THSM] | [TUSS] | [Código ou Não se aplica] |

*(Inserir bloco regulatório se for Musicoterapia ou Psicomotricidade).*
*(Inserir pergunta de seguimento para grupo/casal/familiar).*

### Estrutura B (Coletiva - Grupo / Casal / Familiar):
| Terapia | GRUPO | CASAL | FAMILIAR |
|:---|:---|:---|:---|
| [Nome da Terapia] | [Código] | [Código / Não se aplica] | [Código / Não se aplica] |
