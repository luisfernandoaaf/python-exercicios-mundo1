c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
cor = {'cinza':'\033[0;37m',
       'limite':'\033[m'}
print('A temperatura de {}{}{}ºC corresponde a {}{}{}ºF!'.format(cor['cinza'], c, cor['limite'], cor['cinza'], f, cor['limite']))
