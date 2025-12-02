# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [2.0.0] - 2025-12-02

### Adicionado

#### 🎯 Sistema de Conteúdos Educacionais

- App `contents` para gestão de conteúdos educacionais
- Modelo `Content` com suporte a diferentes tipos (text, video, quiz)
- API REST completa para CRUD de conteúdos
- Sistema de permissões personalizadas (criadores podem editar, todos podem visualizar)
- Testes completos (11 testes) para todas as funcionalidades

#### 📝 Sistema de Quizzes

- App `quizzes` para criação e gestão de questionários
- Modelo `Quiz` com relacionamento one-to-one com conteúdos
- Modelo `Question` com múltiplas opções de resposta
- Sistema de submissão e correção automática de quizzes
- Cálculo de pontuação e feedback para usuários
- Serviço `QuizService` para lógica de negócio
- Testes completos (16 testes) incluindo validações e edge cases

#### 🏆 Sistema de Rankings

- App `rankings` para gestão de pontuações e classificações
- Modelo `UserScore` para rastreamento de pontos por usuário
- API para visualização de rankings globais
- Serializers para exposição de dados de ranking

#### 👥 Sistema de Autenticação Aprimorado

- Modelo `CustomUser` com tipos de usuário (Creator/Learner)
- Autenticação JWT com `djangorestframework-simplejwt`
- Endpoints de registro, login e perfil
- Testes completos (9 testes) para autenticação

#### 📚 Documentação da API

- Integração com `drf-spectacular` para OpenAPI 3.0
- Interface Swagger UI interativa (`/api/docs/`)
- Interface ReDoc alternativa (`/api/redoc/`)
- Schema OpenAPI disponível (`/api/schema/`)

#### 🧪 Sistema de Testes

- 36 testes implementados usando pytest-django
- Cobertura completa dos endpoints da API
- Testes de modelos, serializers e views
- Testes de permissões e autenticação
- Configuração pytest com `pytest.ini`

### Alterado

- Migração de autenticação para JWT (anteriormente token-based)
- Estrutura do projeto reorganizada em apps modulares
- Configurações de CORS para suporte a aplicações frontend
- Sistema de paginação configurado (20 itens por página)

### Configurações Técnicas

- **Django**: 4+
- **Django REST Framework**: Integração completa
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Autenticação**: JWT com refresh tokens (60min access, 1 dia refresh)
- **CORS**: Configurado com `django-cors-headers`
- **Static Files**: Whitenoise para servir arquivos estáticos
- **Localização**: Português do Brasil (pt-br), Timezone: Africa/Luanda

### Deploy

- Aplicação disponível em produção: [Kombinu](https://kombinu.onrender.com)
- Documentação API em produção: [Kombinu Docs](https://kombinu.onrender.com/api/docs/)

---

## [1.0.0] - Data Anterior

### Adicionado

- Estrutura inicial do projeto Django
- Configuração básica de apps
- Sistema de autenticação inicial
