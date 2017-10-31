# -*- coding: UTF-8 -*-
# Napiš program, který se pětkrát zeptá na číslo a nejmenší zadané číslo vypíše.

nejmensi = int(input('Zadej cislo:'))

for opakovani in range(3):
    cislo = int(input('Zadej cislo:'))
    if cislo < nejmensi:
        nejmensi = cislo

print('Nejmensi cislo je {}'.format(nejmensi))
