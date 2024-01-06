v = float(input('Velocidade do carro = '))
m = (v - 80) * 7
print('-=-' * 40)
if v > 80.0:
    print('Você foi multado por ultrapassar o limite de velocidade permitido nesta via (80Km/h), você estava com {}Km/h!'.format(v))
    print('Você terá que pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')
print('-=-' * 40)