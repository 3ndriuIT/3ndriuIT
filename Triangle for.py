# Umieść petle for w drugiej petli for wyswietl trojkat

value = int(input('podaj liczbe: '))

for row in range(1, value + 1):
    for kolumna in range(1, value + 1):
        print(kolumna, end=' ')
    print('')
    value -= 1

