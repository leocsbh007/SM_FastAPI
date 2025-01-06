from fastapi import FastAPI

app = FastAPI()

@app.get("/somar")
async def somar(num1:int, num2:int):
    # num1 = 10
    # num2 = 20
    soma = num1+num2
    return {f"Soma {num1} + {num2} = ": f"{soma}"}


@app.get("/subtrair/{num1}&{num2}")
def subtrair(num1:int, num2:int):    
    subtracao = num1-num2
    return {f"Subtração {num1} - {num2} = ": f"{subtracao}"}

@app.get("/dividir/{num1}&{num2}")
def dividir(num1:int, num2:int):
    divisao = num1/num2
    return {f"Divisão {num1} / {num2} = ": f"{divisao}"}


@app.get("/multiplicar/{num1}&{num2}")
def multiplicar(num1:int, num2:int):
    multiplicacao = num1 * num2
    return {f"Multipicação {num1} x {num2} = ": f"{multiplicacao}"}