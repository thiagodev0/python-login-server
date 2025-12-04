# Python Login Server

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Flask](https://img.shields.io/badge/Flask-Active-green)
![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-black)

Sistema de login e cadastro de usuários feito em Python com Flask e SQLite.

## Funcionalidades
- Cadastro de usuários com senha segura (hash)
- Login e logout
- Dashboard protegido
- Mensagens flash para feedback
- Estrutura modular usando Blueprints
- Banco SQLite gerado automaticamente

## Tecnologias
- Python 3.14
- Flask
- Flask-SQLAlchemy
- HTML, CSS, JavaScript (front-end)

## Estrutura do projeto
```

python-login-server/
├── main.py
├── config.py
├── app/
│   ├── **init**.py
│   ├── routes.py
│   ├── auth.py
│   ├── db.py
│   └── models.py
├── templates/
├── static/
├── requirements.txt
└── LICENSE

````

## Como rodar
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/Python-Login-Server.git
````

2. Entre na pasta do projeto:

```bash
cd Python-Login-Server
```

3. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Rode o servidor:

```bash
python main.py
```

6. Acesse no navegador:

```
http://127.0.0.1:5000/
```

## Observações

* O banco SQLite (`site.db`) será criado automaticamente ao iniciar o app.
* Não comite o banco de dados e a pasta `venv` no Git.

## Licença

MIT License
