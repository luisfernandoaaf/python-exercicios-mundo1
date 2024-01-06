v = float(input('Digite a distância em metros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm = v * 1000
print('A medida {}{}{}m em seus múltiplos tem, valor em kilômetros = {:.2f}km \nvalor em hectômetro = {:.2f}hm \nvalor em decâmetro = {:.0f}dam'.format('\033[4;34m', v, '\033[m', km, hm, dam))
print('A medida {}{}{}m em seus submútiplos tem, valor em decímetros = {:.0f}dm \nvalor em centímetros = {:.0f}cm \nvalor em milímetros = {:.0f}mm'.format('\033[4;34m', v, '\033[m', dm, cm, mm))
