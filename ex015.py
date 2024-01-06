km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias alugado? '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é: R$\033[1;47m{:.2f}\033[m'.format(pago))
