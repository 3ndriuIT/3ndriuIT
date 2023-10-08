# Sprawdz czy pesel jest poprawny.

pesel = '92123006553'
p_check = '13791379131'

correct = 0
for number, _ in enumerate(pesel):
    correct += int(pesel[number]) * int(p_check[number])

if str(correct)[-1] == '0':
    print('pesel jest prawidłowy')
else:
    print('Pesel jest zły')
