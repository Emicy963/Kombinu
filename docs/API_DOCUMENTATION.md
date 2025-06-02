# Dokumentação da API Kombinu

## Visão Geral

A API Kombinu é uma plataforma educacional que oferece funcionalidades de gestão de usuários, cursos, quizzes e gamificação.

**Base URL**: `http://localhost:8000/api/`

## Autenticação

A API utiliza autenticação por token. Após fazer login ou registro, você receberá um token que deve ser incluído no header de todas as requisições autenticadas.

### Header de Autenticação

```
Authorization: Token SEU_TOKEN_AQUI
```

---

## Endpoints de Autenticação (`/api/auth/`)

### 1. Registro de Usuário

**POST** `/api/auth/register/`

Cria uma nova conta de usuário.

#### Request Body:

```json
{
  "username": "usuario123",
  "email": "usuario@email.com",
  "first_name": "João",
  "last_name": "Silva",
  "user_type": "student",
  "phone": "123456789",
  "password": "senha123456",
  "password_confirm": "senha123456"
}
```

#### Campos obrigatórios:

- `username` (string): Nome de usuário único
- `email` (string): Email válido
- `password` (string): Senha com pelo menos 8 caracteres
- `password_confirm` (string): Confirmação da senha

#### Campos opcionais:

- `first_name` (string): Primeiro nome
- `last_name` (string): Sobrenome
- `user_type` (string): Tipo de usuário (`student`, `teacher`, `admin`). Default: `student`
- `phone` (string): Número de telefone

#### Response (201 Created):

```json
{
  "user": {
    "id": 1,
    "username": "usuario123",
    "email": "usuario@email.com",
    "first_name": "João",
    "last_name": "Silva",
    "user_type": "student",
    "phone": "123456789",
    "avatar": null,
    "birth_date": null,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 2. Login

**POST** `/api/auth/login/`

Autentica um usuário existente.

#### Request Body

```json
{
  "username": "usuario123",
  "password": "senha123456"
}
```

#### Response (200 OK)

```json
{
  "user": {
    "id": 1,
    "username": "usuario123",
    "email": "usuario@email.com",
    "first_name": "João",
    "last_name": "Silva",
    "user_type": "student",
    "phone": "123456789",
    "avatar": null,
    "birth_date": null,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 3. Logout

**POST** `/api/auth/logout/`

Invalida o token do usuário atual.

**Requer autenticação**: ✅

#### Response (200 OK):

```json
{
  "message": "Logout realizado com sucesso."
}
```

### 4. Perfil do Usuário

**GET/PUT** `/api/auth/profile/`

Visualiza ou atualiza o perfil do usuário logado.

**Requer autenticação**: ✅

#### Response GET (200 OK):

```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "usuario123",
    "email": "usuario@email.com",
    "first_name": "João",
    "last_name": "Silva",
    "user_type": "student",
    "phone": "123456789",
    "avatar": null,
    "birth_date": null,
    "created_at": "2024-01-15T10:30:00Z"
  },
  "bio": "",
  "location": "",
  "preferred_language": "pt",
  "notification_preferences": {}
}
```

#### Request Body PUT:

```json
{
  "bio": "Desenvolvedor apaixonado por tecnologia",
  "location": "Luanda, Angola",
  "preferred_language": "pt",
  "notification_preferences": {
    "email_notifications": true,
    "push_notifications": false
  }
}
```

---

## Endpoints de Cursos (`/api/courses/`)

### 1. Listar Categorias

**GET** `/api/courses/categories/`

Lista todas as categorias de cursos disponíveis.

**Requer autenticação**: ✅

#### Response (200 OK):

```json
[
  {
    "id": 1,
    "name": "Programação",
    "description": "Cursos de desenvolvimento de software",
    "icon": "code",
    "created_at": "2024-01-15T10:00:00Z"
  },
  {
    "id": 2,
    "name": "Design",
    "description": "Cursos de design gráfico e UI/UX",
    "icon": "palette",
    "created_at": "2024-01-15T10:00:00Z"
  }
]
```

### 2. Listar Cursos

**GET** `/api/courses/`

Lista todos os cursos ativos com filtros opcionais.

**Requer autenticação**: ✅

#### Query Parameters:

- `category` (int): ID da categoria para filtrar
- `difficulty` (string): Nível de dificuldade (`beginner`, `intermediate`, `advanced`)

#### Exemplo: `/api/courses/?category=1&difficulty=beginner`

#### Response (200 OK):

```json
[
  {
    "id": 1,
    "title": "Python para Iniciantes",
    "description": "Aprenda Python do zero",
    "category": 1,
    "category_name": "Programação",
    "instructor": 2,
    "instructor_name": "Prof. Maria Santos",
    "thumbnail": "/media/course_thumbnails/python_basic.jpg",
    "difficulty": "beginner",
    "duration_hours": 20,
    "is_active": true,
    "is_offline_available": true,
    "price": "0.00",
    "created_at": "2024-01-15T09:00:00Z",
    "updated_at": "2024-01-15T09:00:00Z",
    "total_lessons": 15,
    "lessons": [
      {
        "id": 1,
        "course": 1,
        "title": "Introdução ao Python",
        "content": "Nesta lição você aprenderá...",
        "lesson_type": "video",
        "video_file": "/media/lesson_videos/intro_python.mp4",
        "duration_minutes": 30,
        "order": 1,
        "is_preview": true,
        "created_at": "2024-01-15T09:00:00Z"
      }
    ]
  }
]
```

### 3. Detalhes do Curso

**GET** `/api/courses/{id}/`

Obtém detalhes completos de um curso específico.

**Requer autenticação**: ✅

#### Response (200 OK):

```json
{
  "id": 1,
  "title": "Python para Iniciantes",
  "description": "Aprenda Python do zero com exemplos práticos...",
  "category": 1,
  "category_name": "Programação",
  "instructor": 2,
  "instructor_name": "Prof. Maria Santos",
  "thumbnail": "/media/course_thumbnails/python_basic.jpg",
  "difficulty": "beginner",
  "duration_hours": 20,
  "is_active": true,
  "is_offline_available": true,
  "price": "0.00",
  "created_at": "2024-01-15T09:00:00Z",
  "updated_at": "2024-01-15T09:00:00Z",
  "total_lessons": 15,
  "lessons": [
    {
      "id": 1,
      "course": 1,
      "title": "Introdução ao Python",
      "content": "Nesta lição você aprenderá os conceitos básicos...",
      "lesson_type": "video",
      "video_file": "/media/lesson_videos/intro_python.mp4",
      "duration_minutes": 30,
      "order": 1,
      "is_preview": true,
      "created_at": "2024-01-15T09:00:00Z"
    }
  ]
}
```

### 4. Inscrever-se em Curso

**POST** `/api/courses/{course_id}/enroll/`

Inscreve o usuário logado em um curso.

**Requer autenticação**: ✅

#### Response (201 Created) - Primeira inscrição:

```json
{
  "message": "Inscrição realizada com sucesso!",
  "enrollment": {
    "id": 1,
    "student": 1,
    "student_name": "João Silva",
    "course": {
      "id": 1,
      "title": "Python para Iniciantes",
      "instructor_name": "Prof. Maria Santos"
    },
    "status": "active",
    "progress_percentage": 0.0,
    "enrolled_at": "2024-01-15T11:00:00Z",
    "completed_at": null
  }
}
```

#### Response (200 OK) - Já inscrito:

```json
{
  "message": "Você já está inscrito neste curso.",
  "enrollment": {
    "id": 1,
    "student": 1,
    "student_name": "João Silva",
    "course": {
      "id": 1,
      "title": "Python para Iniciantes"
    },
    "status": "active",
    "progress_percentage": 25.5,
    "enrolled_at": "2024-01-15T11:00:00Z",
    "completed_at": null
  }
}
```

### 5. Meus Cursos

**GET** `/api/courses/my-courses/`

Lista todos os cursos em que o usuário está inscrito.

**Requer autenticação**: ✅

#### Response (200 OK):

```json
[
  {
    "id": 1,
    "student": 1,
    "student_name": "João Silva",
    "course": {
      "id": 1,
      "title": "Python para Iniciantes",
      "category_name": "Programação",
      "instructor_name": "Prof. Maria Santos",
      "thumbnail": "/media/course_thumbnails/python_basic.jpg",
      "difficulty": "beginner",
      "total_lessons": 15
    },
    "status": "active",
    "progress_percentage": 25.5,
    "enrolled_at": "2024-01-15T11:00:00Z",
    "completed_at": null
  }
]
```

### 6. Atualizar Progresso da Lição

**POST** `/api/courses/lessons/{lesson_id}/progress/`

Atualiza o progresso do usuário em uma lição específica.

**Requer autenticação**: ✅

#### Request Body:

```json
{
  "completion_percentage": 100.0,
  "time_spent_minutes": 30,
  "is_completed": true
}
```

#### Response (200 OK):

```json
{
  "message": "Progresso atualizado com sucesso!",
  "progress": {
    "id": 1,
    "enrollment": 1,
    "lesson": {
      "id": 1,
      "title": "Introdução ao Python",
      "lesson_type": "video",
      "duration_minutes": 30
    },
    "is_completed": true,
    "completion_percentage": 100.0,
    "time_spent_minutes": 30,
    "completed_at": "2024-01-15T12:00:00Z"
  },
  "course_progress": 33.3
}
```

---

## Códigos de Erro Comuns

### 400 Bad Request

```json
{
  "error": "Dados inválidos fornecidos"
}
```

### 401 Unauthorized

```json
{
  "detail": "As credenciais de autenticação não foram fornecidas."
}
```

### 403 Forbidden

```json
{
  "detail": "Você não tem permissão para executar essa ação."
}
```

### 404 Not Found

```json
{
  "detail": "Não encontrado."
}
```

### 500 Internal Server Error

```json
{
  "error": "Erro interno do servidor"
}
```

---

## Exemplos de Uso

### 1. Fluxo Completo de Registro e Inscrição em Curso

```javascript
// 1. Registrar usuário
const registerResponse = await fetch('/api/auth/register/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'joao123',
    email: 'joao@email.com',
    first_name: 'João',
    last_name: 'Silva',
    password: 'senha123456',
    password_confirm: 'senha123456'
  })
});

const { user, token } = await registerResponse.json();

// 2. Listar cursos disponíveis
const coursesResponse = await fetch('/api/courses/', {
  headers: {
    'Authorization': `Token ${token}`
  }
});

const courses = await coursesResponse.json();

// 3. Inscrever-se em um curso
const enrollResponse = await fetch(`/api/courses/${courses[0].id}/enroll/`, {
  method: 'POST',
  headers: {
    'Authorization': `Token ${token}`
  }
});

const enrollmentData = await enrollResponse.json();
```

### 2. Acompanhar Progresso

```javascript
// Atualizar progresso de uma lição
const progressResponse = await fetch('/api/courses/lessons/1/progress/', {
  method: 'POST',
  headers: {
    'Authorization': `Token ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    completion_percentage: 100,
    time_spent_minutes: 25,
    is_completed: true
  })
});

const progressData = await progressResponse.json();
console.log(`Progresso do curso: ${progressData.course_progress}%`);
```

---
