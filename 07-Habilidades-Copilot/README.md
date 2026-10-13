# Habilidades Modulares para o Microsoft 365 Copilot 🏥⚡

Esta pasta contém o ecossistema completo de **15 Habilidades (Skills)** estruturadas especificamente para o novo recurso de agentes modulares do **Microsoft 365 Copilot** (Agent Builder / Copilot Studio).

---

## 📂 Visão Geral das 15 Habilidades

```text
07-Habilidades-Copilot/
├── 01-Fisioterapia-Completa/          # Família Fisioterapia (TUSS + THSM + Manual + DUT 24)
├── 02-Negativas-Glosas/               # Família Negativas (TUSS + THSM + CSV oficial + N305)
├── 03-Complementos-Pendencias/        # Família Complementos (A101 a A213A + CSV oficial + A150)
├── 04-Texto-Livre-Aprimorado/         # Família Texto Livre (Modelos Aprovados + Anti-alucinação)
├── 05-Bonus-Pedido-Fisioterapia/      # Bônus Sequencial: Pedido Médico + Codificação Fisioterapia
├── 06-Bonus-Pedido-Notas-Nutricao/    # Bônus Sequencial: Pedido Médico + Nota Técnica Nutrição (DUT 18/12/6)
├── 07-Encontrar-TUSS-Rol-DUT/         # Codificação TUSS + Rol ANS (Sim/Não) + DUTs Clínicas
├── 08-Conselho-Profissional/          # Consulta Pública em Conselhos (CREFITOs, CRFas, CFP, CFN)
├── 09-Especialidade-Medica-RQE/       # Identificação Médica Oficial (CFM/CRM + RQEs + Áreas de Atuação)
├── 10-Auditoria-Notas-Fiscais/        # Autenticidade de NFS-e (Prefeituras / MEI Nacional) e NF-e (SEFAZ)
├── 11-Analise-Notas-Terapias/         # Emissão de Notas Técnicas (Nutrição DUT 108 + Terapias ACP)
├── 12-Extracao-Pedido-Medico/         # OCR e Extração Estruturada de Pedidos Médicos (Tabela Vertical)
├── 13-Codigos-Terapias/               # Códigos Oficiais de Terapias (Individuais, Coletivas e Telessaúde)
├── 14-CID-Diagnosticos/               # Codificação e Validação em CID-10 e CID-11 (Cartões Visuais)
├── 15-Calculo-Vacina-SCAM/            # Cálculo Reverso do Item C (Coeficiente) no Sistema SCAM
├── build_skills.py                    # Script de automação e reempacotamento de ZIPs
└── README.md                          # Este guia operacional
```

---

## 🚀 Como Configurar no Copilot 365

1. **Criar o Agente:**
   * Acesse o Microsoft 365 Copilot ou Copilot Studio e clique em **Criar Agente**.
2. **Definir as Instruções (Maestro 8K):**
   * Abra o arquivo `INSTRUCOES_COPILOT_8K.md` da habilidade desejada;
   * Copie o texto completo e cole na caixa **"Instruções" (Instructions)** do agente.
3. **Carregar a Habilidade (`.zip`):**
   * No painel de configuração do agente, vá até a seção **"Habilidades" (Skills)**;
   * Clique em **"Carregar habilidade" (Upload a skill)**;
   * Selecione o arquivo `.zip` correspondente (ex.: `07-Encontrar-TUSS-Rol-DUT.zip`);
   * O Copilot validará automaticamente o `SKILL.md` e indexará os arquivos da pasta `references/`.
4. **Salvar e Publicar:**
   * Salve o agente e inicie os testes na caixa de diálogo.

---

## 🔄 Manutenção e Atualização Futura

Caso uma tabela, manual ou diretriz da ANS seja atualizado:
1. Atualize o arquivo correspondente na subpasta `references/`;
2. Execute o script de empacotamento:
   ```bash
   python3 build_skills.py
   ```
3. O script validará o YAML e regerará todos os arquivos `.zip` atualizados automaticamente.
