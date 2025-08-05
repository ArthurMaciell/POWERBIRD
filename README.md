# 🐦 PowerBird

PowerBird é uma solução de automação de dados que integra informações do **RD Station CRM** e do **Bling ERP**, organiza essas informações em planilhas Excel e prepara os dados para análise no **Power BI**.

## 🚀 Objetivo

Facilitar e automatizar a coleta, estruturação e integração de dados de vendas e negociações, permitindo relatórios mais rápidos e confiáveis no Power BI.

## ⚙️ Principais Funcionalidades

- 📅 Coleta automática de negociações do RD Station via API
- 🔗 Integração com o Bling (futuro ou já incluso)
- 📊 Expansão e normalização dos campos personalizados do RD Station
- 📁 Geração de planilhas Excel estruturadas
- 🔄 Aplicação de regras de negócio com scripts customizados (`ajustar_dist`, `ajustar_rep`)
- 📈 Preparação dos dados para dashboards no Power BI
- 📝 Registro de logs de execução

## 📂 Estrutura do Projeto

```
PowerBird/
├── data/                 # Planilhas geradas
├── logs/                 # Registros de execução
├── scripts/
│   ├── ajuste_dist.py
│   └── ajuste_rep.py
├── utils/
│   └── auth.py           # Token OAuth2 do RD Station
├── main.py               # Script principal de extração e tratamento
└── README.md
```

## 🧪 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/ArthurMaciell/POWERBIRD.git
cd PowerBird
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Obs: certifique-se de que você configurou corretamente o token de autenticação no arquivo `utils/auth.py`.

### 4. Execute o script principal

```bash
python main.py
```

A planilha será gerada na pasta `data/` (ou no caminho configurado).

## 🧐 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [requests](https://requests.readthedocs.io/)
- [RD Station API](https://developers.rdstation.com/)
- [Power BI](https://powerbi.microsoft.com/)

## ✅ Próximos passos

-

## 📌 Exemplo de uso no Power BI

1. Execute o `main.py`
2. Abra o Power BI e conecte-se à planilha `.xlsx` gerada
3. Atualize o dashboard com os dados mais recentes

---

## 👨‍💻 Autor

**Seu Nome**\
LinkedIn: [Arthur Maciel](linkedin.com/in/arthur-maciel6325)

