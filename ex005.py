n = int(input('Digite seu número: '))
print('O seu número é {}{}{}. Seu antecessor é {} e seu sucessor é {}'.format('\033[1;4;42m', n, '\033[m', n-1, n+1))