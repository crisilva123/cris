import requests
# import para trazer a função que deseja
# request ele buscar em algum lugar

texto = requests.get("https://viacep.com.br/ws/01001000/json/")
# texto é a variavel pode ser qualquer uma
# requests é a função
# get para chamar a função
# o site tem que colocar entre aspas para ele ler

data = texto.json()
# data , só um nome para a função
# texto a variavel de cima
# json , é o jeito que ele vai trazer a informação para você

print(data)
# print, só para chamar a função 

print(data["logradouro"])
# neste caso vai buscar a informação do site e te responde somente o que você pediu