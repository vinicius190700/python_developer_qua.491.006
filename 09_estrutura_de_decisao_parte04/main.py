#declaraçâo de variaveis
nome = input("Informe sua nome: ")
idade = int(input("Informe sua idade: "))

#ternaria
result = "é maior de idade." if idade>= 18 else "é menor de idade."

#saide
print(f"{nome} {result}")