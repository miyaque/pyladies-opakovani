# -*- coding: UTF-8 -*-
# Ověř, že je vstupní řetězec palindrom, tedy, že se čte zepředu stejně jako
# od konce. Příklady: "nepotopen", "kajak", "oko"

def je_palindrom(text):
    for i in range(len(text)//2):
        if vstup[i] != vstup[-1 - i]:
            return False
    return True

vstup = input('Zadej slovo: ')

if je_palindrom(vstup):
    print('{} je palindrom'.format(vstup))
else:
    print('{} není palindrom'.format(vstup))
