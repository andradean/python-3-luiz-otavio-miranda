def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5) 
print(multiplicação)

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'

    return f'{numero} é impar'

print(par_impar(5))
print(par_impar(42))
print(par_impar(44))
print(par_impar(77))
        