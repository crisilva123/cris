import requests
# tem que instalar co comand pront o request

cep = input("Digite seu cep:  ")
# criei uma variavel para buscar o cep que vai ser digitado

Response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
# joguei a variavel dentro do site, que realiza a busca e me retorna o endereço

data = Response.json()

print(data)