from random import randint
from time import sleep
pc = randint(0, 5) # Faz o pc "Pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei?')) # Jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == pc:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(pc, jogador))


