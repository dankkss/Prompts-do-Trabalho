# Habilidades Modulares para o Microsoft 365 Copilot 🏥⚡

Esta pasta contém os pacotes de **Habilidades (Skills)** estruturados especificamente para o novo recurso de agentes modulares do **Microsoft 365 Copilot** (Agent Builder / Copilot Studio).

---

## 📂 Estrutura do Diretório

```text
07-Habilidades-Copilot/
├── 01-Fisioterapia-Completa/          # Família Fisioterapia (TUSS + THSM + Manual + DUT 24)
│   ├── SKILL.md
│   ├── INSTRUCOES_COPILOT_8K.md
│   ├── 01-Fisioterapia-Completa.zip
│   └── references/
├── 02-Negativas-Glosas/               # Família Negativas (TUSS + THSM + CSV oficial + N305)
│   ├── SKILL.md
│   ├── INSTRUCOES_COPILOT_8K.md
│   ├── 02-Negativas-Glosas.zip
│   └── references/
├── 03-Complementos-Pendencias/        # Família Complementos (A101 a A213A + CSV oficial + A150)
│   ├── SKILL.md
│   ├── INSTRUCOES_COPILOT_8K.md
│   ├── 03-Complementos-Pendencias.zip
│   └── references/
├── 04-Texto-Livre-Aprimorado/         # Família Texto Livre (Modelos Aprovados + Anti-alucinação)
│   ├── SKILL.md
│   ├── INSTRUCOES_COPILOT_8K.md
│   ├── 04-Texto-Livre-Aprimorado.zip
│   └── references/
├── 05-Bonus-Pedido-Fisioterapia/      # Bônus Sequencial: Pedido Médico + Codificação Fisioterapia
│   ├── SKILL.md
│   ├── INSTRUCOES_COPILOT_8K.md
│   ├── 05-Bonus-Pedido-Fisioterapia.zip
│   └── references/
├── 06-Bonus-Pedido-Notas-Nutricao/    # Bônus Sequencial: Pedido Médico + Nota Técnica Nutrição (DUT 18/12/6)
│   ├── SKILL.md
│   ├── INSTRUCOES_COPILOT_8K.md
│   ├── 06-Bonus-Pedido-Notas-Nutricao.zip
│   └── references/
├── build_skills.py                    # Script de automação e reempacotamento de ZIPs
└── README.md                          # Este guia operacional
```

---

## 🚀 Como Configurar no Copilot 365

1. **Criar o Agente:**
   * Acesse o Microsoft 365 Copilot ou Copilot Studio e clique em **Criar Agente**.
2. **Definir as Instruções (Maestro 8K):**
   * Abra o arquivo `INSTRUCOES_COPILOT_8K.md` da família desejada;
   * Copie o texto completo e cole na caixa **"Instruções" (Instructions)** do agente.
3. **Carregar a Habilidade (`.zip`):**
   * No painel de configuração do agente, vá até a seção **"Habilidades" (Skills)**;
   * Clique em **"Carregar habilidade" (Upload a skill)**;
   * Selecione o arquivo `.zip` correspondente (ex.: `01-Fisioterapia-Completa.zip`);
   * O Copilot validará automaticamente o `SKILL.md` e indexará os arquivos da pasta `references/`.
4. **Salvar e Publicar:**
   * Salve o agente e inicie os testes enviando pedidos médicos ou notas de fisioterapia.

---

## 🔄 Manutenção e Atualização Futura

Caso uma tabela ou manual seja atualizado (ex.: nova versão de críticas ou novas resoluções):
1. Atualize o arquivo correspondente na subpasta `references/`;
2. Execute o script de empacotamento:
   ```bash
   python3 build_skills.py
   ```
3. O script validará o YAML e regerará os arquivos `.zip` atualizados automaticamente.
