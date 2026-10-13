# CATÁLOGO DE PORTAIS TRIBUTÁRIOS, SISTEMAS FISCAIS E REGRAS DE CONSULTA

Este guia reúne as regras de localização, validação e plataformas para auditoria de autenticidade de Notas Fiscais de Serviços (NFS-e) e Notas Fiscais de Produtos/Materiais (NF-e).

---

## 1. CLASSIFICAÇÃO DO TIPO DE DOCUMENTO FISCAL

### 1.1 NFS-e Municipal (Serviços em Geral)
- **Escopo:** Consultas médicas, sessões de fisioterapia, psicologia, fonoaudiologia, nutrição, exames, honorários médicos e taxas hospitalares.
- **Canal Oficial:** Portal da PREFEITURA MUNICIPAL onde o serviço foi prestado ou plataforma arrecadadora terceirizada contratada pelo município.
- **Caso Especial Brasília / Distrito Federal:**
  * O DF não possui prefeitura municipal.
  * A consulta de NFS-e do DF é realizada exclusivamente no portal da **SEFAZ-DF (Receita DF - ISS/NFS-e)**.

### 1.2 NFS-e de MEI (Microempreendedor Individual)
- **Notas a partir de 01/09/2023:** Obrigatoriamente emitidas e consultadas no **Portal Nacional da NFS-e**:
  `https://www.nfse.gov.br/ConsultaPublica`
- **Notas anteriores a 01/09/2023:** Podem requerer consulta no portal da prefeitura local ou no portal nacional.

### 1.3 NF-e Estadual (Produtos, Medicamentos, Órteses, Próteses e OPME)
- **Escopo:** Materiais cirúrgicos, próteses, medicamentos de alto custo e insumos hospitalares.
- **Canal Oficial:** **Portal Nacional da NF-e** (`https://www.nfe.fazenda.gov.br`) via Chave de Acesso de 44 dígitos OU no portal da SEFAZ Estadual (`sefaz.[uf].gov.br`).
- **Regra Rígida:** NUNCA buscar prefeitura municipal para NF-e de materiais/produtos.

### 1.4 Chave Indeterminada
- Se a entrada for apenas uma chave de 44 dígitos numéricos => Tratar diretamente como NF-e de Produtos (Portal Nacional da NF-e).
- Se a entrada contiver código de verificação curto + CNPJ/Prestador => Tratar como NFS-e municipal.

---

## 2. PRINCIPAIS PLATAFORMAS HOMOLOGADAS DE PREFEITURAS
Muitos municípios não possuem portal próprio e terceirizam o sistema de NFS-e para empresas especializadas. Links dessas plataformas são oficiais desde que direcionados à instância da cidade:
- **WebISS:** Utilizado por dezenas de capitais e grandes cidades (ex: Salvador, Belo Horizonte, etc.).
- **Giss Online / Ginfes:** Plataforma amplamente adotada em SP e diversas regiões.
- **Betha Sistemas (Fly e-Nota):** Muito comum no Sul e Sudeste.
- **ISSNet / Nota Control:** Utilizado em cidades do Centro-Oeste e Sudeste (ex: Campo Grande).
- **Atende.Net (IPM Sistemas):** Presente em centenas de municípios do Sul do país.
- **DSF:** Utilizado em capitais como São Paulo, Campinas e Teresina.
- **SimplISS / SigISS / Sigcorp / Tributus / Ciga / GovDigital / Pronim.**

---

## 3. DESAMBIGUAÇÃO DE MUNICÍPIOS HOMÔNIMOS
- Se o município informado existir em mais de um estado brasileiro (ex: São José, Belém, Bonito, Santa Rosa, Boa Vista, Palmeira):
  * Se houver UF, CNPJ da clínica ou endereço no documento => Fixar o estado e seguir normalmente.
  * Se houver APENAS o nome da cidade sem UF e sem CNPJ => Não pesquisar e solicitar:
    `"Existem municípios com esse nome em mais de um estado. Por favor, informe o estado (UF) ou o CNPJ da clínica para identificação correta."`
- Se informado apenas o CNPJ, pesquise o cadastro público do CNPJ para descobrir a cidade e estado e siga direto para a busca da nota.
