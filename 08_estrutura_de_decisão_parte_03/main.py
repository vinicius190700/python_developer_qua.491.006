#declaraçao de variaveis
aluno = input("Digite seu nome do aluno: ")
media = float(input("informe a média do aluno: ").replace(",", "."))

#Estrutura de decisão
if media >= 0 or media <= 10:
    if media >= 7:
        print(f"{aluno} está aprovado.")
    
    elif media >= 5:
        print(f"{aluno} está de recuperação.")
    else:
        
        print(f"{aluno} está reprovado.")


else:
     print("Nota invalida.")