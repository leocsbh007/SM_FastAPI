import requests

cep = '30627230'
url = f"https://cep.awesomeapi.com.br/json/{cep}"

resposta = requests.get(url)


print(resposta.status_code)
print(resposta.headers)
print("===========================================")
print(resposta.text)