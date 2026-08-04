# Y-CSV-Backend

API backend construída com **FastAPI** para processamento de arquivos CSV, desenvolvida como par do [Y-CSV](https://github.com/yannickcruz/Y-CSV) (editor de CSV em React). O serviço recebe, processa e manipula dados tabulares no servidor usando `pandas`, expondo endpoints REST consumidos pelo front-end.

## ✨ Funcionalidades

- **Upload de arquivos CSV** — endpoint para envio de arquivos via `multipart/form-data` (`python-multipart`).
- **Processamento de dados com pandas** — leitura, transformação e manipulação de datasets CSV no servidor.
- **Limite de tamanho de arquivo** — middleware customizado que rejeita uploads acima de **20 MB**, retornando `413 Request Entity Too Large`.
- **CORS habilitado** — configurado para aceitar requisições de qualquer origem, facilitando a integração com o front-end hospedado separadamente (ex.: Render).
- **Validação de dados com Pydantic** — schemas tipados para validar entradas e padronizar as respostas da API.
- **Arquitetura em camadas** — separação clara entre rotas (`api/routers`), configurações (`core`), modelos de dados (`schemas`) e lógica de negócio (`services`).
- **Configuração centralizada** — nome da aplicação, versão, host e porta definidos via `core.configs.settings`.
- **Endpoint de health-check** — rota raiz (`GET /`) retornando o status da API.

> A lista completa de endpoints para manipulação de CSV está em `api/routers/csv_router.py` — consulte o código-fonte para detalhes de cada rota.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web para construção da API |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI para executar a aplicação |
| [Pandas](https://pandas.pydata.org/) | Leitura, manipulação e processamento dos dados CSV |
| [Pydantic](https://docs.pydantic.dev/) | Validação de dados e definição de schemas |
| [python-multipart](https://github.com/andrew-d/python-multipart) | Suporte a upload de arquivos (`multipart/form-data`) |

## 📁 Estrutura do projeto

```
Y-CSV-Backend/
├── api/
│   └── routers/       # Rotas da API (endpoints relacionados a CSV)
├── core/               # Configurações da aplicação (settings, host, porta, versão)
├── schemas/            # Modelos Pydantic para validação de dados
├── services/           # Lógica de negócio / processamento dos arquivos
├── main.py             # Ponto de entrada da aplicação (FastAPI app)
├── __init__.py
└── requirements.txt     # Dependências do projeto
```

## 🚀 Como executar localmente

Pré-requisitos: [Python 3.10+](https://www.python.org/) e `pip`.

```bash
# Clone o repositório
git clone https://github.com/yannickcruz/Y-CSV-Backend.git
cd Y-CSV-Backend

# (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python main.py
```

Por padrão, a API ficará disponível em `http://localhost:<PORT>` (host e porta definidos em `core/configs.py`).

Você também pode iniciar via Uvicorn diretamente:

```bash
uvicorn main:app --reload
```

A documentação interativa gerada automaticamente pelo FastAPI fica disponível em:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## 🔗 Projeto relacionado

- **Front-end:** [Y-CSV](https://github.com/yannickcruz/Y-CSV) — aplicação React que consome esta API.
