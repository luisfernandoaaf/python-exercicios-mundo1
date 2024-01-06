
# Método 1 de cores:
print('\033[30;107mOlá, Mundo\033[m!!!')

# Método 2 de cores:
n = 'Luis'
print('Bom dia Sr. {}{}{}!!!'.format('\033[43m', n, '\033[m'))

# Método 3 de cores:
nome = 'Luis'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;97m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))