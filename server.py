from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return{ "message": "Hello World "}

@app.get("/profile/{name}")
async def saudacao (name: str):
    texto = f'Olá, {name}'
    return{ "message": texto}

@app.post("/profile")
async def root ():
    return{ "name": "Lea Sampaio"}

@app.post("/dobro")
async def calculadora(num :int):
    resultado = num * 2
    return f"O dobro de {num} é {resultado}"