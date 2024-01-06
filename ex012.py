p = float(input('Qual o preço inicial do seu produto?'))
d = p - (p * 5 / 100)
print('O produto que custava \033[4;36mR${:.2f}\033[m, na promoção com desconto de 5% vai custar \033[4;36mR${:.2f}\033[m'.format(p, d))
