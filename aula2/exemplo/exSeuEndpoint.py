import requests 

nome = 'Leo'
url = f"http://localhost:8000/tasks"

headers = {'Content-Type' : 'application/json'}

payload = {
    'task': 'Estudar FastAPI'
}

resposta = requests.post(url, headers=headers, json=payload)

print(resposta.status_code)
print(resposta.headers)
print(resposta.text)