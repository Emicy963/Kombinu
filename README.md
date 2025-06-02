# Kombinu - Plataforma Educacional

Sistema Django com API REST para gestão de cursos, usuários, quizzes e gamificação educacional.

## 🌐 Aplicação Online

A aplicação está disponível online em: **[https://kombinu.onrender.com](https://kombinu.onrender.com)**

### Acesso Rápido à Documentação da API

- **Documentação Swagger**: [https://kombinu.onrender.com/api/docs/](https://kombinu.onrender.com/api/docs/)
- **Documentação ReDoc**: [https://kombinu.onrender.com/api/redoc/](https://kombinu.onrender.com/api/redoc/)
- **Schema OpenAPI**: [https://kombinu.onrender.com/api/schema/](https://kombinu.onrender.com/api/schema/)

## Funcionalidades

### Sistema Web

- Sistema de autenticação completo (login, registro, logout)
- Dashboard protegido para usuários autenticados
- Interface responsiva e intuitiva
- Mensagens de feedback para os usuários

### API REST

- **Autenticação por Token**: Sistema seguro de autenticação
- **Gestão de Usuários**: Registro, login, perfis e preferências
- **Cursos e Categorias**: Sistema completo de gestão educacional
- **Progresso de Aprendizagem**: Acompanhamento detalhado do progresso
- **Inscrições**: Sistema de matrícula em cursos
- **Documentação Interativa**: Swagger/OpenAPI integrado

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

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as migrações do banco de dados:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor:**

   ```bash
   python manage.py runserver
   ```

7. **Acesse o sistema localmente:**

   - **Página inicial**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **Dashboard**: [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
   - **Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
   - **API Docs (Swagger)**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
   - **API Schema**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)

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
