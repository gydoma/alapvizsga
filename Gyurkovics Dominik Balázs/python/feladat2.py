print('Paradicsom:  1199Ft/Kg')
print('Paprika:     1349Ft/Kg')
print('Vöröshagyma:  289Ft/Kg')
ker = None
keszadag = 0
while ker != 'nem':
    ker = input('Kíván valamit vásárolni? ')
    if ker == 'igen':
        mibol = input('     Melyik termékből? ')
        adag = float(input(f'     Hány Kg {mibol}(o)t szeretne? '))
        if mibol == 'paradicsom': kgadag = 1199
        elif mibol == 'paprika': kgadag = 1349
        elif mibol == 'vöröshagyma': kgadag = 289
        keszadag = keszadag + kgadag * adag
print('Köszönjük a vásárlást!')
print(f'Fizetendő összeg: {int(round(keszadag, 0))}Ft')