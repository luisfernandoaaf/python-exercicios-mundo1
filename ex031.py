d = float(input('Qual a distância de sua viagem em Km? '))
vc = d * 0.50
vl = d * 0.45
if d <= 200:
    print('Na sua viagem curta (de até a 200Km) você irá pagar R${:.2f}'.format(vc))
else:   
    print('Na sua viagem longa (maior que 200km) você irá pagar R${:.2f}'.format(vl))