nome = input('Qual o seu nome: ')
ano_nascimento = int(input('digite ano de nascimento: '))
ano_atual =  int(input('digite o ano atual: '))
idade = ano_atual - ano_nascimento
print(f'olá {nome}, bem vindo a valhalla, você tem {idade} anos')