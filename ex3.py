notas = int(input("Quantas notas você deseja inserir? "))
nota = []
soma = 0

for i in range(notas):
    n = float(input(f"Digite a nota {i+1}: "))
    nota.append(n)
    soma += n

print(f"A soma das notas é: {soma}")