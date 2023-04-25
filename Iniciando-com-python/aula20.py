nome_user = input("Digite o seu nome: ")
idade_user = input("Digite a sua idade: ")
caractere = len(nome_user) 
espaco = " " in nome_user

if nome_user  and idade_user:
    print(f'Seu nome é: {nome_user} \n seu nome invertido é: {nome_user[::-1]}')
    print(f'seu nome tem {caractere} letras')
    print(f'a primeira letra do seu nome é {nome_user[0]}')
    print(f'a ultima letra do seu nome é {nome_user[-1]}')
else:
    print("Desculpe, você não digitou nada")
   
if espaco:
    print("Seu nome contém espaços")
else:
    print("Seu nome não contém espaços")
    



