#entrada de dadps
nome = input("informe seu nome: ")
idade= int(input("informe sua idade: "))
altura = float(input("informe sua altura em metros: ").replace(',', '.'))

#saída de dados
print(f"Seja bem vindo ao curso de python, {nome}!")
print(f"idade do usuario: {idade}.")
print(f"altura do usuario: {altura} metros.")

#verificando o tipo de dados
print(f"{nome}: {type(nome)}.")   
print(f"{idade}: {type(idade)}.")
print(f"{altura}: {type(altura)}.")
