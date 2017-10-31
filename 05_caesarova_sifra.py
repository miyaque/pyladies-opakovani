posun = int(input('Zadej cislo: '))
text = input('Zadej text k zasifrovani: ')

sifrovany_text = ''
for pismeno in text:
    pismeno = pismeno.lower()
    pozice = ord(pismeno) + posun
    if pozice > ord('z'):
        pozice -= 26
    sifrovany_text += chr(pozice)

print(sifrovany_text)
