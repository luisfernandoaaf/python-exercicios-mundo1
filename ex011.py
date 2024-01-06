l = float(input('Digite a largura da sua parede:'))
a = float(input('Digite a altura de sua parede:'))
ar = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, a, ar))
t = ar / 2
cor = {'Magenta':'\033[1;45m',
     'limite':'\033[m'}
print('Para pintar essa parede você precisará de {}{}{}l de tinta.'.format(cor['Magenta'], t, cor['limite']))

