slownik = {}

string = 'raz raz raz raz dwa dwa dwa trzy trzy cztery'
podzielone = string.split(' ')
print(podzielone)

for wyraz in podzielone:
    if wyraz not in slownik:
       slownik[wyraz] = 0

    slownik[wyraz] += 1
print(slownik)










