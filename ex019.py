import random
#from random import choice
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
sorteado = random.choice(alunos)
#sorteado = choice(alunos)
print('O aluno sorteado foi {}{}{}'.format('\033[1;97;42m', sorteado, '\033[m'))
