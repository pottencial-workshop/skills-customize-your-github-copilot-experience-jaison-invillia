"""Starter code para a tarefa FastAPI REST APIs.

Instruções:
1. Instale dependências (se necessário): pip install fastapi uvicorn
2. Implemente os endpoints CRUD para /books
3. Substitua a lista em memória por algo mais persistente opcionalmente
4. Adicione validação com modelos Pydantic
"""

from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field
import datetime

app = FastAPI(title="FastAPI REST APIs Assignment", description="CRUD de livros com validação e tratamento de erros.")

# Modelos Pydantic (estudante pode ajustar conforme tarefas)
class BookIn(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., ge=1900, le=datetime.datetime.now().year)

class Book(BookIn):
    id: int

# Armazenamento em memória
books: List[Book] = []
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

# TODO: Implementar endpoints abaixo
# @app.get("/books")
# def list_books():
#     return books

# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     ...

# @app.post("/books", status_code=201)
# def create_book(book: BookIn):
#     ...

# @app.put("/books/{book_id}")
# def update_book(book_id: int, book: BookIn):
#     ...

# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     ...

# Dica: Use HTTPException(status_code=404, detail="Book not found") quando apropriado.
# Executar: uvicorn starter-code:app --reload
