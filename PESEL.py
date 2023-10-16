# Check your identification number ! 

pesel = input('Wpisz swoj nr pesel: ')
check = '13791379131'

control = 0
# for number, _ in enumerate(pesel):
#     correct += int(pesel[number]) * int(p_check[number])
# BEZ ZIPPA !

for pesel_digit, check_digit in zip(pesel, check):
    control += int(pesel_digit) * int(check_digit)

# if str(control)[-1] == '0':
#     print('pesel jest prawidłowy')
# else:
#     print('Pesel jest zły')

print("pesel jest ok!") if str(control)[-1] == '0' else print('pesel jest zly!')
