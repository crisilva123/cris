soma = 0
negativo = 0

print("Digite 8 números inteiros: ")
for i in range(1,9):
    numero = int(input(f"Número {i}: "))
    if numero < 0:
        negativo += 1
    else:
        soma += numero

print(f"Quantidade de números negativos: {negativo}")
print(f"Soma dos números positivos: {soma}")