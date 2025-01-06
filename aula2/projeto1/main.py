from fastapi import FastAPI

app = FastAPI()

banco_de_dados = []
@app.get("/tasks")
async def get_task():
     return {"tasks":[d for d in banco_de_dados]} 