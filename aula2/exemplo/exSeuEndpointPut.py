import requests 

id = 1
url = f"http://localhost:8000/tasks/{id}"
headers = {'Content-Type' : 'application/json'}
dados = {
    'task': 'Estudar Programação Cplus-plus'
}

resposta = requests.put(url, headers=headers, json=dados)

print(resposta.status_code)
print(resposta.headers)
print(resposta.text)