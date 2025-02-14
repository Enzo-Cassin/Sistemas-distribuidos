from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

contatos = list()

class Contato(BaseModel):
    nome: str
    numero: int
    email: str

@app.get("/")
def root():
    return contatos


@app.get("/contatos/{pos}")
def get_tarefa(pos: int):
    return contatos[pos]

@app.post("/adicionar/")
def criar_contato(contato: Contato):
    contato.feito = False
    contatos.append(contato)
    return len(contato)

@app.delete("/deletar/{pos}")
def deletar_contato(pos: int):
    contato = contatos.pop(pos)
    return contato
