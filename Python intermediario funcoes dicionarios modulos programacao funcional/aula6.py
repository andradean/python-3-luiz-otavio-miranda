def calc(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = calc(2)
triplicar = calc(3)
quadruplicar = calc(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))

    