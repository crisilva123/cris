pares = 0
impares = 0

for n in range (1,11) :
    inteiro = int(input("Insira um numero inteiro:  "))
    if inteiro % 2 == 0 :
        pares = pares +1
    else :
        impares = impares +1

print (f"numeros pares são {pares} ")
print(f"numeros impares são {impares}")            
print(f"todos os numeros {inteiro}")     