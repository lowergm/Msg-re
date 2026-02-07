# Mini Chat FastAPI

Um chat simples feito com FastAPI e Tortoise ORM.
Permite enviar mensagens através de um form HTML, salvar no banco de dados e renderizar na página. 

---
## Estrutura do projeto
```
/Msg-re
|-- main.py
|-- router.py
|-- models.py
|-- templates/
|---- index.html
|-- static/
|---- style.css
```
---

## Pré-requisitos

- Python 3.9+  
- Pip ou Pipenv  
- SQLite (ou outro banco de dados, configurável via `.env`)  

---

## Instalação

1. Clonar o repositório:

```bash
git clone https://github.com/lowergm/Msg-re.git
cd Msg-re
```

2. Instalar dependências:
```bash
pip install fastapi tortoise-orm uvicorn python-dotenv python-multipart
```

3. Rodar:
```bash
uvicorn main:app
```

- Acessar no navegador:
`http://localhost:8000`

## Estrutura das mensagens
*Cada mensagem tem*:
- `id`: identificador único
- `mensagem`: conteúdo enviado pelo usuário
- `criado_em`: data e hora de criação (UTC)

Feito com ❤️ por Lower :D
