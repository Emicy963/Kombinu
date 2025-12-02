# Kombinu - Plataforma Educacional

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.0+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Sistema Django com API REST para gestão de conteúdos educacionais, quizzes interativos, rankings e gamificação.

> 📝 **Novidades da v2.0**: Confira todas as mudanças no [CHANGELOG.md](CHANGELOG.md)

## 🌐 Aplicação Online

A aplicação está disponível online em: **[https://kombinu.onrender.com](https://kombinu.onrender.com)**

### Acesso Rápido à Documentação da API

- **Documentação Swagger**: [https://kombinu.onrender.com/api/docs/](https://kombinu.onrender.com/api/docs/)
- **Documentação ReDoc**: [https://kombinu.onrender.com/api/redoc/](https://kombinu.onrender.com/api/redoc/)
- **Schema OpenAPI**: [https://kombinu.onrender.com/api/schema/](https://kombinu.onrender.com/api/schema/)

## Funcionalidades

### 🎯 Sistema de Conteúdos
- Gestão completa de conteúdos educacionais (texto, vídeo, quiz)
- Sistema de permissões (criadores podem editar, todos podem visualizar)
- API REST para CRUD completo

### 📝 Sistema de Quizzes
- Criação e gestão de questionários interativos
- Múltiplas opções de resposta por pergunta
- Submissão e correção automática
- Cálculo de pontuação e feedback

### 🏆 Sistema de Rankings
- Rastreamento de pontuações por usuário
- Rankings globais
- Gamificação educacional

### 👥 Autenticação
- **JWT Authentication**: Sistema seguro com tokens de acesso e refresh
- **Tipos de Usuário**: Creator (criador de conteúdo) e Learner (estudante)
- **Gestão de Perfis**: Registro, login e gerenciamento de perfil

### 📚 Documentação da API
- **Swagger UI**: Interface interativa para testar endpoints
- **ReDoc**: Documentação alternativa elegante
- **OpenAPI 3.0**: Schema completo disponível

## Requisitos

Antes de iniciar, certifique-se de ter instalado:

- Python 3.8+
- Django 4+
- Django REST Framework
- Pip e virtualenv (recomendado)

## Instalação e Configuração

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/Emcy963/Kombinu.git
   cd Kombinu
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Configure as variáveis de ambiente:**

   ```bash
   # Copie o arquivo de exemplo
   copy .env.example .env  # Windows
   # cp .env.example .env  # Linux/macOS
   
   # Edite o arquivo .env e configure:
   # - SECRET_KEY (gere uma nova chave)
   # - DEBUG=True (para desenvolvimento)
   # - ALLOWED_HOSTS=localhost,127.0.0.1
   ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure as migrações do banco de dados:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor:**

   ```bash
   python manage.py runserver
   ```

8. **Acesse o sistema localmente:**

   - **API Docs (Swagger)**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
   - **API ReDoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
   - **Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Testes

O projeto possui uma suíte completa de testes usando pytest.

### Executando os Testes

```bash
# Executar todos os testes
pytest

# Executar com verbose
pytest -v

# Executar testes de um app específico
pytest apps/accounts/tests.py
pytest apps/contents/tests.py
pytest apps/quizzes/tests.py

# Executar com cobertura (requer pytest-cov)
pytest --cov=apps
```

### Cobertura de Testes

- **accounts**: 9 testes (autenticação e perfis)
- **contents**: 11 testes (CRUD e permissões)
- **quizzes**: 16 testes (criação, submissão e validação)
- **Total**: 36 testes ✅

## Estrutura do Projeto

```
Kombinu/
├── accounts/              # App de autenticação
│   ├── migrations/
│   ├── templates/accounts/
│   ├── views.py          # Views web
│   ├── api.py           # Views da API
│   ├── urls.py          # URLs web
│   ├── urls_api.py      # URLs da API
│   ├── models.py
│   └── forms.py
├── courses/              # App de cursos
│   ├── migrations/
│   ├── views.py         # Views da API de cursos
│   ├── urls.py          # URLs da API de cursos
│   ├── models.py
│   └── serializers.py
├── dashboard/            # App do dashboard
│   ├── templates/dashboard/
│   ├── views.py
│   └── urls.py
├── templates/           # Templates globais
│   └── base.html
├── static/             # Arquivos estáticos
├── media/              # Arquivos de mídia
├── manage.py
├── requirements.txt
└── README.md
```

## Rotas Principais

### Interface Web

| Rota | Descrição |
|------|-----------|
| `/` | Página inicial |
| `/login/` | Login de usuários |
| `/dashboard/` | Dashboard (requer login) |
| `/termos_condicoes/` | Termos e condições |

### API REST

| Rota | Descrição |
|------|-----------|
| `/api/auth/register/` | Registro de usuários |
| `/api/auth/login/` | Login (obter token) |
| `/api/auth/logout/` | Logout (invalidar token) |
| `/api/auth/profile/` | Perfil do usuário |
| `/api/courses/` | Listar cursos |
| `/api/courses/{id}/` | Detalhes do curso |
| `/api/courses/categories/` | Categorias de cursos |
| `/api/courses/my-courses/` | Meus cursos |
| `/api/courses/{id}/enroll/` | Inscrever-se em curso |

### Documentação

| Rota | Descrição | URL de Produção |
|------|-----------|----------------|
| `/api/docs/` | Documentação Swagger | [https://kombinu.onrender.com/api/docs/](https://kombinu.onrender.com/api/docs/) |
| `/api/redoc/` | Documentação ReDoc | [https://kombinu.onrender.com/api/redoc/](https://kombinu.onrender.com/api/redoc/) |
| `/api/schema/` | Schema OpenAPI | [https://kombinu.onrender.com/api/schema/](https://kombinu.onrender.com/api/schema/) |

## Testando a API

### Ambiente de Produção

Para testar a API diretamente no ambiente de produção, utilize a base URL:
```
https://kombinu.onrender.com/api/
```

### Exemplo de Uso

```bash
# Registrar um novo usuário
curl -X POST https://kombinu.onrender.com/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword123"
  }'

# Fazer login
curl -X POST https://kombinu.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "securepassword123"
  }'
```

## Documentação da API

Para informações detalhadas sobre como usar a API, consulte nossa **[Documentação da API](docs/API_DOCUMENTATION.md)** que inclui:

- Guia completo de endpoints
- Exemplos de requisições e respostas
- Códigos de erro e suas descrições
- Fluxos de uso comuns
- Boas práticas de implementação

Você também pode acessar a documentação interativa através das rotas:
- **Produção**: 

[https://kombinu.onrender.com/api/docs/](https://kombinu.onrender.com/api/docs/) (Swagger) ou [https://kombinu.onrender.com/api/redoc/](https://kombinu.onrender.com/api/redoc/) (ReDoc)

- **Desenvolvimento**: `/api/docs/` (Swagger) ou `/api/redoc/` (ReDoc)

## Tecnologias Utilizadas

- **Backend**: Django 4+, Django REST Framework
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Autenticação**: Token-based authentication
- **Documentação**: drf-spectacular (OpenAPI/Swagger)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deploy**: Render (Produção)

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autores

### Chefe do Projeto

- **Anderson Cafurica** - *Desenvolvedor Principal*
  - GitHub: [@Emicy963](https://github.com/Emicy963)
  - Email: andersonpaulo931@gmail.com
  - LinkedIn: [Anderson Cafurica](https://linkedin.com/in/anderson-cafurica)

### Equipe de Desenvolvimento

- **DOMAG Tech** - *Desenvolvimento e Suporte*

## Contato

Se tiver alguma dúvida, sugestão ou quiser contribuir com o projeto, entre em contato através do GitHub ou pelos contatos do chefe do projeto listados acima.

---

**Kombinu** - Transformando a educação através da tecnologia 🚀

**🌐 Acesse agora**: [https://kombinu.onrender.com](https://kombinu.onrender.com)
