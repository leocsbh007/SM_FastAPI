import requests 

nome = 'Leo'
url = f"http://localhost:8000/tasks"
headers = {'Content-Type' : 'application/json'}
json = {
    'task': {
        'id':'1',
        'tarefa' : 'Estudar Programação C++',
        'completada' : 'False',
    }
}

resposta = requests.post(url, headers=headers, params=json)

print(json)
print(resposta.status_code)
print(resposta.headers)
print(resposta.text)