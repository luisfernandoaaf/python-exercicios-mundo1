'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é: {}'.format(num, trunc(num)))'''

num = float((input('Digite um valor: ')))
print('O valor digitado foi: {}{}{} e a sua porção inteira é: {}{}{}'.format('\033[4;30;41m', num, '\033[m', '\033[4;30;41m', int(num), '\033[m'))

