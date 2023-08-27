# Words counter


slownik = {}

string = input('Proszę podać tekst do podliczenia: ')
podzielone = string.split(' ')

for wyraz in podzielone:
    if wyraz not in slownik:
       slownik[wyraz] = 0

    slownik[wyraz] += 1
print(slownik)










