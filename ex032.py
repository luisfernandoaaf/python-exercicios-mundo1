a = int(input('Digite o ano: '))
b = a % 4
if b == 0:
    print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto'.format(a))
