import pyfiglet as pyf
# pyf somente um "apelido" para não ter que digitar a palvra inteira

var =input ("Digite qual palavra você deseja:  ")
# peço a informação para o usuario
# var é a variavel (um pote para cria a variavel)

palavra = pyf.figlet_format(var)
print(palavra)
# palavra é a variavel para ter oonde armazenar o arquivo