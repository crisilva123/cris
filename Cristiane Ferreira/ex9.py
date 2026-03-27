inicial = int(input("Digite um numero inteiro:  "))
Final = int(input("Digite outro numero inteiro:  "))

for i in range(inicial, Final + 1) :
    for n in range (1,11):
        print(f'tabuada do {n} x {i} = {n} x {i}')