soma = 0
cont = 0
for c in range(0,6):
    n = int(input('Digite o {} valor...'.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você ifnromou {} número pares e a soma foi {}'.format(cont,soma))