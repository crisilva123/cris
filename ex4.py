maior = None
menor = None

for i in range(1,11):
    num = int(input(f"Digite o número {i+1}: "))
    
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
    
