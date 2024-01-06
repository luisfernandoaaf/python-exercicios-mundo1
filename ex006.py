n = int(input('Digite seu número: '))
cor = {'amarelo':'\033[0;33m',
       'limite':'\033[m'}
print('O dobro de {} é: {}'.format(n, n*2))
print('O triplo de {} é: {}'.format(n, n*3))
print('A raiz quadrade de {}{}{} é: {}{:.2f}{}'.format(cor['amarelo'], n, cor['limite'] , cor['amarelo'] ,n**(1/2), cor['limite']))