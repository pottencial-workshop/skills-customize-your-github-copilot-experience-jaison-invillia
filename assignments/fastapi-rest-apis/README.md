# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective
Construir uma API REST usando FastAPI com operações CRUD completas, modelos de validação (Pydantic) e tratamento adequado de erros HTTP.

## 📝 Tasks

### 🛠️ Setup & CRUD Básico

#### Description
Configurar um projeto FastAPI mínimo e implementar endpoints CRUD para um recurso simples (por exemplo: `Book`). Cada livro deve ter `id`, `title`, `author`, `year`.

#### Requirements
Completed program should:

- Iniciar um app FastAPI acessível em `http://localhost:8000`
- Expor endpoints: `GET /books`, `GET /books/{id}`, `POST /books`, `PUT /books/{id}`, `DELETE /books/{id}`
- Usar lista em memória para armazenamento inicial
- Validar que `title` e `author` não estão vazios
- Retornar `404` para livro não encontrado
- Retornar `201` ao criar e incluir JSON do livro

### 🛠️ Validação, Erros e Melhorias

#### Description
Adicionar modelos Pydantic para entrada/saída, validar campos e melhorar respostas de erro. Incluir um endpoint de saúde e documentação adicional.

#### Requirements
Completed program should:

- Usar `BookIn` (entrada) e `Book` (saída) como modelos Pydantic
- Garantir que `year` seja inteiro entre 1900 e o ano atual
- Retornar mensagens claras em erros de validação
- Adicionar endpoint `GET /health` que retorna `{ "status": "ok" }`
- Incluir exemplo de resposta de erro customizada
- Organizar código em funções para cada operação

```bash
# Execução esperada (após implementação pelo estudante)
uvicorn app:app --reload
```

> Dica: Após finalizar CRUD básico, considere substituir o armazenamento por uma estrutura de dados mais eficiente ou persistência simples em arquivo JSON.
