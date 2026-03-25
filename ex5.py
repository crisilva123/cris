nomes = []
for i in range(1,6):
    nome = input(f"Digite o nome {i}: ")
    nomes.append(nome)

print("Os nomes digitados são:")
for nome in nomes:
    print(nome)

print(f"Primeiro nome: {nomes[0]}")
print(f"Último nome: {nomes[-1]}")