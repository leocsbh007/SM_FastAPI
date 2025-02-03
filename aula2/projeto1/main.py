from fastapi import FastAPI

app = FastAPI()

banco_de_dados = [
     
]
@app.get("/tasks")
async def get_task():
     return {"tasks":[d for d in banco_de_dados]} 


@app.post("/tasks")
async def create_task(task:str):
     banco_de_dados.append(task)
     return {"message" : f"Tarefa '{task}' criada com sucesso"}

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task : str):
     for item in banco_de_dados:
          print(item)
     return {"message": f"Tarefa {task_id} atualizada para '{task}'"}
