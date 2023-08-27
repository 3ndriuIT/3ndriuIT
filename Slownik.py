
print('Dostępne w słowniku: ')
dictionary = {
    'jabłko': 'apple',
    'brzoskwiniaa': 'peach',
    'banan': 'banana',
    'winogrono': 'grape',
    'pomarancza': 'orange',

}
dictionary2 = {}
for polskie , angielskie in dictionary.items():
    dictionary2[angielskie] = polskie

    print(f'polskie: {polskie}, \t angielskie: {angielskie}')

word = (input('\nWybierz tłumacznie na angielski [1] na polski [2] \n'))
if word not in ['1', '2']:
    print('Nie rozumiem, spróbuj jeszcze raz')
    quit()
if word == '1':
    pick = input('wpisz słowo po polsku aby przetłumaczyć na angielski: ')
    if pick not in dictionary:
        print('Nie ma takiego słowa w słowniku! ')
        quit()
    print(f'To oznacza: {dictionary[pick]}')

else:
    pick2 = input('wpisz słowo po angielsku aby przetłumczyc na polski: ')
    if pick2 not in dictionary2:
        print('Nie ma takiego słowa w słowniku! ')
        quit()
    print(f' To oznacza {dictionary2[pick2]}')