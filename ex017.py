from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
cor = {'vermelhoepreto':'\033[1;4;31;40m',
       'limite':'\033[m'}
print('A hipotenusa vai medir: {}{:.2f}{}'.format(cor['vermelhoepreto'], hi, cor['limite']))
'''import math
catoposto = float(input('Valor do cateto oposto do t.retângulo: '))
catadjacente = float(input('Valor do cateto adjacente: '))
cop = catoposto ** 2
cad = catadjacente ** 2
hip = math.sqrt(cop + cad)
print('A hipotenusa do t.retângulo é: {:.0f}'.format(hip))'''