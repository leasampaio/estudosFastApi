from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional [str]
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List = []

@app.get('/')
def home():
    return {"msg": "tudo ok"}

@app.post("/animais")
def cadastrar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append((animal))
    return animal


@app.get("/animais")
def retornar_animais():
    return banco

@app.get("/animais/{id}")
def retorna_animal(id: str):
    for animal in banco:
        if animal.id == id:
            return animal
    return {"erro": "Animal não localizado"}

    

@app.delete("/animais/{id}")
def  apagar_animal(id: str):
    posicao = -1
    for index, animal in enumerate(banco):
        if animal.id == id:
            posicao = index
            break
    if posicao != -1:
        banco.pop(posicao)
        return "Deletado!"
    else:
        return {"erro": "Animal não localizado"}
    