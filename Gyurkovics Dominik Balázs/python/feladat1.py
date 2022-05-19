from audioop import reverse


szoveg = input('Írjon be egy legalább 9 karakterből álló szöveget: ')
if len(szoveg) > 8:
    print(szoveg[::-1].lower())
else: print(f'a(z) {szoveg} kevesebb, mint 9 karakter hosszú') 