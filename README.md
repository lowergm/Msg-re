# Msg-re
Chat feito usando FastAPI, PostgreSQL, TortoiseORM, Jinja2 com o objetivo de estudar mais sobre essas tecnologias

---
## Estrutura do projeto
```
/Msg-re/
|-- main.py
|-- router.py
|-- models.py
|-- requeriments.txt
|-- templates/
|---- index.html
|-- static/
|---- style.css
```
---
main.py - registrar rotas + banco de dados
router.py - rotas do projeto
models.py - tabelas do banco de dados
requirements.txt - bibliotecas usadas no projeto
templates/index.html - interface do projeto - mostrar as mensagens e formulário para mandar novas mensagens pro banco
static/style.css - estilização do front-end

---
## Instalação
1. Clonar repositório:
```bash
git clone https://github.com/lowergm/Msg-re/
cd Msg-re
```

2. Instalar dependências:
```bash
pip install -r requirements.txt
```

3. Rodar o site:
```bash
uvicorn main:app --reload
```
Abra o site em `http://localhost:8000`

---
## Estrutura do banco
*Cada mensagem tem*:
`id`: Identificador único de cada mensagem
`mensagem`: Mensagem enviada pelo usuário
`criado_em`: Horário e dia que uma mensagem foi enviada
