# Hádání čísla je hra dvou hráčů. Jeden si myslí skryté číslo v určitém
# intervalu a druhý se jej snaží uhádnout. Na zadaný tip, odpovídá první hráč
# pouze tím, zda je skryté číslo větší nebo menší než tipované.
# Prvního hráče simulujte počítačem.

from random import randint

cislo = randint(0, 20)


while True:
    tip = input('Hadej cislo mezi 0 a 20: ')
    while not tip.isdigit():
        tip = input('Nezadals cislo. Zkus to znovu(0 az 20): ')
    tip = int(tip)

    if tip < 0 or tip > 20:
        print('Jsi mimo rozmezi.')
    elif tip == cislo:
        print('Gratuluju. Uhodls!')
        break
    elif tip < cislo:
        print('Hadane cislo je větší.')
    else:
        print('Hadane cislo je menší.')

print('Skryte cislo bylo {}'.format(cislo))
