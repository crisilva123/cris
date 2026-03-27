nomes = []

print("  MENU ")
print("1- Cadastrar nome")
print("2- Lista de nomes")
print("3- Sair")

while True :
   
    opcao = input(" digite a opção desejada:   ")

    if opcao == "1" :
        nome = input("Digite seu nome:   ")
        nomes.append(nome)
        print(f"Nome {nomes} cadastrado com sucesso")

    elif opcao == "2":
        print(f"Lista de nomes {nomes} ")
        # if nomes == 0:
        #     print("Opcao invalidade, tente novamente")
         
        # else:
        #     print("Lista de nomes ")
        #     for n in nome:
        #         print("-") 

    elif opcao == "3":
        print ("saindo do sistema")
        break
        
    # else:
    #     print("Nome cadastrado")   


   
