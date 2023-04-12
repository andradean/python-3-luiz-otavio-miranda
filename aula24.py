"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('digite um numero: ')
is_int = numero.isdecimal()

if is_int == True:
    numero = int(numero)

if is_int == True and numero % 2 == 0:
    print('numero é par')
elif is_int == True and numero % 2 != 0:
    print(f'numero é impar')
else:
    print('voce nao digitou um numero inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hour = input('Que horas são? ')

verify = ':' in hour 
if verify:
    hour = int(hour[:2])

if verify == False:
    print("digite o horario corretamente")
elif hour >= 0 and hour <= 11:
    print('bom dia')
elif hour >= 12 and hour <= 17:
     print('boa tarde')
elif hour >= 18 and hour <= 23:
    print('boa noite')
else: 
    print('digite o horario corretamente')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("digite seu nome: ")
nome_tamanho = len(nome)

if nome_tamanho <= 4:
    print('seu nome é curto')
elif nome_tamanho == 5 or nome_tamanho == 6:
    print('seu nome é normal')
elif nome_tamanho > 6:
    print('seu nome é muito grande')
else:
    print('----------')