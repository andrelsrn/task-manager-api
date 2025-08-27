# Task Manager API

## Descrição
Uma API RESTful simples e robusta para gerenciamento de usuários e tarefas, desenvolvida com FastAPI e SQLAlchemy. Esta API permite criar, ler, atualizar e deletar usuários e suas respectivas tarefas, oferecendo uma base sólida para aplicações de gerenciamento de fluxo de trabalho.

## Funcionalidades
*   **Gerenciamento de Usuários (CRUD)**: Crie, visualize, atualize e delete usuários.
*   **Gerenciamento de Tarefas (CRUD)**: Crie, visualize, atualize e delete tarefas, com atribuição a usuários.
*   **Segurança de Senhas**: Armazenamento seguro de senhas com hashing (bcrypt).
*   **Validação de Dados**: Validação automática de dados de entrada e saída com Pydantic.
*   **Persistência de Dados**: Utiliza SQLite como banco de dados, configurável para outros SGBDs.
*   **Documentação Interativa da API**: Documentação Swagger UI e ReDoc gerada automaticamente.

## Tecnologias Utilizadas
*   **Python**: Linguagem de programação principal.
*   **FastAPI**: Framework web moderno e rápido para construir APIs.
*   **SQLAlchemy**: ORM (Object Relational Mapper) para interação com o banco de dados.
*   **Pydantic**: Biblioteca para validação de dados e configurações.
*   **Uvicorn**: Servidor ASGI de alta performance.
*   **Passlib**: Biblioteca para hashing de senhas.

## Configuração e Instalação

Siga os passos abaixo para configurar e rodar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/andrelsrn/task-manager-api.git
    cd task-manager-api
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv .venv
    # No Windows
    .venv\Scripts\activate
    # No macOS/Linux
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicialize o banco de dados:**
    O banco de dados SQLite (`task_manager.db`) será criado automaticamente na primeira execução da aplicação, e as tabelas serão geradas com base nos modelos definidos.

## Uso

Para iniciar o servidor da API, execute o seguinte comando na raiz do projeto:

```bash
uvicorn src.main:app --reload
```

O servidor estará disponível em `http://127.0.0.1:8000`.

### Documentação da API
Acesse a documentação interativa da API para testar os endpoints:
*   **Swagger UI**: `http://127.0.0.1:8000/docs`
*   **ReDoc**: `http://127.0.0.1:8000/redoc`

### Exemplo de Interação (via Swagger UI)

1.  **Criar um Usuário:**
    *   Vá para `http://127.0.0.1:8000/docs`.
    *   Expanda o endpoint `POST /users/`.
    *   Clique em "Try it out".
    *   No campo "Request body", insira os dados do usuário (ex: `{"name": "João Silva", "email": "joao.silva@example.com", "role": "user", "password": "senhaSegura123"}`).
    *   Clique em "Execute".

2.  **Criar uma Tarefa:**
    *   Expanda o endpoint `POST /tasks/`.
    *   Clique em "Try it out".
    *   No campo "Request body", insira os dados da tarefa, incluindo o `id` do usuário criado (ex: `{"title": "Comprar Leite", "description": "Leite integral", "status": "not_started", "priority": "high", "assignee_id": 1}`).
    *   Clique em "Execute".

## Endpoints da API

### Usuários
*   `POST /users/`: Cria um novo usuário.
*   `GET /users/`: Lista todos os usuários.
*   `GET /users/{user_id}`: Retorna um usuário específico pelo ID.
*   `PUT /users/{user_id}`: Atualiza um usuário existente.
*   `DELETE /users/{user_id}`: Deleta um usuário.

### Tarefas
*   `POST /tasks/`: Cria uma nova tarefa.
*   `GET /tasks/`: Lista todas as tarefas.
*   `GET /tasks/{task_id}`: Retorna uma tarefa específica pelo ID.
*   `PUT /tasks/{task_id}`: Atualiza uma tarefa existente.
*   `DELETE /tasks/{task_id}`: Deleta uma tarefa.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
