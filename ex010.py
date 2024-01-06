real = float(input('Quanto dinheiro você tem em sua carteira? '))
dolar = real / 3.27
print('Com {}R${:.2f}{} você pode comprar US$:{}{:.2f}{}'.format('\033[0;35m', real, '\033[m', '\033[0;35m', dolar, '\033[m'))
