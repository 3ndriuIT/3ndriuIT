# BMI measure
# BMI = weight / (height in meters) ** 2

height = int(input('jaki jest twoj wzrost[cm]: ' ))
weight = float(input('ile wazysz[kg]: ' ))



print(f'for height {height} and weight {weight} BMI is ')
BMI = (float(weight/ (height/100) ** 2))
print(f'BMI is {BMI:.2f}')
print(f'BMI is {round(BMI, 2)}')