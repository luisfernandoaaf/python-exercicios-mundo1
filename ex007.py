n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
med = (n1+n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a \033[1;43m{:.1f}\033[m'.format(n1, n2, med))