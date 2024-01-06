salário = float(input('Quanto seu funcionário ganha? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava {}R${:.2f}{}, com 15% de aumento, passa a receber {}R${:.2f}{}'.format('\033[1;4;46m', salário, '\033[m', '\033[1;4;46m', novo, '\033[m'))
