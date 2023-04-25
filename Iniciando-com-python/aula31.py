
palavra_secreta = 'tijolo'
letra_acertada = ''

while True:
    letra = input('digite uma letra: ')
    
    if len(letra) > 1:
        print('digite apenas uma letra')
        continue
    
    if letra in palavra_secreta:
        letra_acertada += letra
        
    for letra in palavra_secreta:
        if letra in letra_acertada:
            print(letra)
        else:
            print('*')