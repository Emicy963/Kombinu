# Projeto Django - Sistema de Autenticação e Dashboard

Este é um projeto Django que implementa um sistema de autenticação de usuários com login, registro e dashboard protegido.

## Funcionalidades

- Cadastro de usuários
- Login e logout
- Redirecionamento para um dashboard protegido
- Mensagens de feedback para os usuários

## Requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.8+
- Django 4+
- Pip e virtualenv (recomendado)

## Instalação e Configuração

1. Clone este repositório:

   ```sh
   git clone https://github.com/Emcy963/Kombinu.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Configure as migrações do banco de dados:

   ```sh
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o painel de administração:

   ```sh
   python manage.py createsuperuser
   ```

6. Inicie o servidor:

   ```sh
   python manage.py runserver
   ```

7. Acesse o sistema no navegador:
   - Página inicial: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Estrutura do Projeto

```bash
Kombinu/
│── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── forms.py
│── dashboard/
│   ├── templates/dashboard/
│   ├── views.py
│   ├── urls.py
│── templates/
│   ├── base.html
│── manage.py
│── requirements.txt
│── README.md
```

## Rotas Principais

| Rota          | Descrição |
|--------------|------------|
| `/`          | Página inicial |
| `/accounts/register/` | Registro de user-admin |
| `/accounts/login/`    | Login de user-admin |
| `/accounts/logout/`   | Logout |
| `/dashboard/`  | Dashboard (requer login) |

## Contato

Se tiver alguma dúvida ou sugestão, entre em contato pelo GitHub!

## Autor

DOMAG Tech
