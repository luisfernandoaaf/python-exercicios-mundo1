n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
cor = {'vermelhoeciano':'\033[1;31;40m',
     'limite':'\033[m'}
print('A soma entre {} e {} é igual a {}{}{}!'.format(n1, n2, cor['vermelhoeciano'], s, cor['limite']))