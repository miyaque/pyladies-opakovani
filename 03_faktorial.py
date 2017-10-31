# -*- coding: UTF-8 -*-
# Napiš program pro výpočet faktoriálu čísla zadaného uživatelem
# Zkus použít for i while cyklus

n = int(input('faktorial pro n: '))

faktorial = 1

for i in range(n):
    faktorial *= i + 1

# varianta s while cyklem

#while n:
#    faktorial = faktorial * n
#    n = n - 1

print('Faktorial čísla {} je {}'.format(n, faktorial))
