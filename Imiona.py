# Popros usera o podanie imienia. W zaleznosci od jego ostatniej litery wyswietl:
# 'Witam Pana" lub "Witam Panią".
user = input('Podaj swoje imie:')

if user[-1] == 'a':
    print('Witam Panią')
else:
    print('Witam Pana')


