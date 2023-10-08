# Palindromy (słowa które z obydwu stron czyta sie tak samo)

pal1 = input('podaj pierwszy wyraz: ')
pal2 = input('podaj drugi wyraz: ')
pal1 = ''.join(pal1.split(' '))
pal2 = ''.join(pal2.split(' '))
# ta funkcja pozbywa się spacji pomiedzy słowami !!

if pal1 == pal2[::-1]:
    print('To są palindromy!')
else:
    print('To nie są palindromy!')