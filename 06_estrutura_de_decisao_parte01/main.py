#declaração de variaveis
nome= input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura= float(input("Digite sua altura em metros: ").replace(",", "."))

#estrutura de decisão
if idade >= 12 and altura >= 1.15:
    print(f"{nome} está autorizado a entra.")

else:
    print(f"{nome} não está autorizado a entrar.")
 