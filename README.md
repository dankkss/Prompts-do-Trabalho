# Prompts do Trabalho 🏥📋

Repositório contendo o ecossistema completo de agentes, prompts, tabelas e manuais de regulação em saúde, auditoria de reembolso médico e codificação TUSS/THSM. Estruturado para uso direto no **Google Gemini** e **Microsoft Copilot**.

---

## 📂 Estrutura do Repositório

```text
Prompts-do-Trabalho/
├── 00-Planilhas-e-Tabelas-Base/
│   ├── Críticas_Análise_2026.xlsx       # Planilha mestre institucional (26/01/2026)
│   └── csv_tabelas/                     # Exportações em CSV para consulta direta no GitHub
│       ├── Complemento_atualizado_26.01.26.csv
│       ├── NEGATIVAS_complemento_26.01.26.csv
│       ├── N305.csv
│       ├── A150.csv
│       ├── CÓDIGOS_CONSULTA.csv
│       ├── CÓDIGOS_TERAPIAS.csv
│       ├── CÓDIGOS_FISIOTERAPIA.csv
│       ├── Reembolso_Especifico.csv
│       ├── TEXTO_LIVRE.csv
│       ├── DICAS.csv
│       └── Criticas_sistemicas.csv
├── 01-CID-e-TUSS/
│   ├── CID Final.md
│   ├── Códigos Terapia Final.md
│   └── Encontrar TUSS Final.md
├── 02-Fisioterapia/
│   ├── Análise Fisioterapia Final.md
│   ├── Fisioterapia Reconstruída Final.md
│   ├── Fisioterapia THSM Copilot Final.md
│   ├── Fisioterapia TUSS Copilot Final.md
│   └── Manual de Fisioterapia.pdf       # Manual operacional oficial em PDF
├── 03-Negativas/
│   ├── Negativa THSM Copilot Final.md
│   ├── Negativa THSM Gemini Final.md
│   ├── Negativa TUSS Copilot Final.md   # Inclui crítica 290 CP
│   └── Negativa TUSS Gemini Final.md    # Inclui crítica 290 CP
├── 04-Conselhos-e-Especialidades/
│   ├── Conselho Copilot Final.md
│   ├── Conselho Gemini Final.md
│   ├── Especialidade Copilot Final.md
│   └── Especialidade Gemini Final.md
├── 05-Notas-e-Documentos/
│   ├── Encontrar Nota Fiscal Final.md
│   ├── Notas Copilot Final.md
│   ├── Notas Gemini Final.md
│   ├── Pedido Médico Copilot Final.md
│   └── Pedido Médico Gemini Final.md
├── 06-Pareceres-e-Complementos/
│   ├── Complemento Copilot Final.md
│   ├── Complemento Gemini Final.md
│   ├── Texto Livre Copilot Final.md
│   ├── Texto Livre Gemini Final.md
│   └── Vacina Final.md
├── 07-Habilidades-Copilot/              # Pacotes de Habilidades modulares (.zip + SKILL.md) para Copilot 365
│   ├── 01-Fisioterapia-Completa/        # Família Fisioterapia (TUSS + THSM + Manual + DUT 24)
│   ├── build_skills.py                  # Script de automação e reempacotamento de ZIPs
│   └── README.md
└── originais_gem/
    └── [25 arquivos .gem originais nomeados individualmente para backup/importação]
```

---

## 📑 Catálogo de Agentes (25 Prompts + Planilha Mestre + Manual)

| Categoria | Agente / Arquivo | Plataforma | Finalidade Operacional |
|---|---|---|---|
| **00. Base** | `Críticas_Análise_2026.xlsx` | Excel / CSV | Catálogo mestre institucional de críticas, complementos e negativas. |
| **01. CID e TUSS** | `CID Final.md` | Universal | Mapeamento e validação de diagnósticos da CID-10 e diretrizes clínicas. |
| **01. CID e TUSS** | `Encontrar TUSS Final.md` | Universal | Localização e correspondência de procedimentos na Tabela TUSS. |
| **01. CID e TUSS** | `Códigos Terapia Final.md` | Universal | Codificação e regras de cobertura para terapias multidisciplinares (psico, fono, TO). |
| **02. Fisioterapia** | `Análise Fisioterapia Final.md` | Universal | Análise clínica e documental completa de solicitações de fisioterapia. |
| **02. Fisioterapia** | `Fisioterapia Reconstruída Final.md` | Gemini (Expandido) | Regras aprofundadas de segmentação anatômica, diretrizes e codificação fisioterapêutica. |
| **02. Fisioterapia** | `Fisioterapia TUSS Copilot Final.md` | Copilot | Codificação TUSS para procedimentos e sessões de fisioterapia. |
| **02. Fisioterapia** | `Fisioterapia THSM Copilot Final.md` | Copilot | Codificação THSM (Tabela Hospitalar e Serviços Médicos). |
| **02. Fisioterapia** | `Manual de Fisioterapia.pdf` | Manual PDF | Referência técnica oficial para embasamento dos critérios regulatórios. |
| **03. Negativas** | `Negativa TUSS Copilot Final.md` | Copilot | Aplicação de glosas/motivos de negativa (N) em contratos TUSS (inclui crítica 290 CP). |
| **03. Negativas** | `Negativa TUSS Gemini Final.md` | Gemini | Aplicação de glosas/motivos de negativa (N) em contratos TUSS (inclui crítica 290 CP). |
| **03. Negativas** | `Negativa THSM Copilot Final.md` | Copilot | Aplicação de glosas/motivos de negativa (N) em contratos THSM. |
| **03. Negativas** | `Negativa THSM Gemini Final.md` | Gemini | Aplicação de glosas/motivos de negativa (N) em contratos THSM. |
| **04. Conselhos & Esp.** | `Conselho Copilot Final.md` | Copilot | Validação de registro profissional em conselhos de classe (CRM, CRO, CREFITO, CRP). |
| **04. Conselhos & Esp.** | `Conselho Gemini Final.md` | Gemini | Validação cadastral e conferência aprofundada de prestadores. |
| **04. Conselhos & Esp.** | `Especialidade Copilot Final.md` | Copilot | Verificação de Registro de Qualificação de Especialista (RQE) e especialidades médicas. |
| **04. Conselhos & Esp.** | `Especialidade Gemini Final.md` | Gemini | Conferência aprofundada de titulações médicas para fins de cobertura. |
| **05. Notas & Docs** | `Encontrar Nota Fiscal Final.md` | Universal | Localização e validação de portais emissores de NFS-e e NF-e municipais/estaduais. |
| **05. Notas & Docs** | `Notas Copilot Final.md` | Copilot | Emissão de notas técnicas de auditoria de nutrição e terapias com ACP. |
| **05. Notas & Docs** | `Notas Gemini Final.md` | Gemini | Redação detalhada de laudos e notas técnicas de auditoria. |
| **05. Notas & Docs** | `Pedido Médico Copilot Final.md` | Copilot | Extração e auditoria de requisitos obrigatórios em pedidos médicos/odontológicos. |
| **05. Notas & Docs** | `Pedido Médico Gemini Final.md` | Gemini | Análise aprofundada de conformidade em prescrições médicas. |
| **06. Pareceres** | `Complemento Copilot Final.md` | Copilot | Críticas de complemento (pendência documental - A) para instrução do processo. |
| **06. Pareceres** | `Complemento Gemini Final.md` | Gemini | Guia expandido de complementos e desempate de pendências operacionais. |
| **06. Pareceres** | `Texto Livre Copilot Final.md` | Copilot | Redação administrativa padrão para comunicação formal com o segurado. |
| **06. Pareceres** | `Texto Livre Gemini Final.md` | Gemini | Elaboração de textos livres objetivos para notificações ao beneficiário. |
| **06. Pareceres** | `Vacina Final.md` | Universal | Análise de cobertura e cálculo de vacinas no sistema de regulação. |
| **07. Habilidades M365** | `01-Fisioterapia-Completa/` | Copilot 365 (Skill) | Pacote modular (.zip) unificando TUSS, THSM, Manual e DUT 24. |

---

## 🔒 Privacidade e Segurança

- Repositório 100% privado (`--private`) sob a conta `@dankkss`.
- Dados estritamente operacionais e regulatórios, sem quaisquer dados pessoais ou senhas.
- Sincronização executada exclusivamente via conexão Wi-Fi.

---

## 💡 Formatos Disponíveis

1. **Markdown (`.md`):** Formato principal para visualização no GitHub, edição ágil e cópia rápida para qualquer IA (Gemini, Copilot, ChatGPT, Claude).
2. **Arquivos `.gem` Originais:** Armazenados na pasta `originais_gem/`, preservando a estrutura protobuf do Google para caso seja necessária a restauração ou reimportação direta no Google Gems.
3. **Planilha Mestre (`.xlsx` e `.csv`):** Disponível em formato nativo do Excel e desmembrada em arquivos `.csv` para consulta textual direta no GitHub.
