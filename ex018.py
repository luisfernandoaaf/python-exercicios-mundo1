from math import radians, sin, cos, tan
a = float(input('Digite o valor do ângulo: ',))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo \033[0;32;107m{}\033[m tem seno = \033[0;32;107m{:.2f}\033[m \nCosseno = \033[0;32;107m{:.2f}\033[m \nE tangente = \033[0;32;107m{:.2f}\033[m'.format(a, s, c, t))
