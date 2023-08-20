# Small store


products = {
            'ak47': 2000,
            'mp40': 1300,
            'awp':  4500,
            'm4a1': 3400,
            'deagle': 700,
            'grenade': 300,
            'smoke': 300,
            'molotov': 700,
            'kevlar': 1000,
            'p250': 300,
}
print('Hello, here you have our list of items: ')

for name, cost in products.items():
    print(f' product: {name} \t price: {cost}')

product = input('Which one do You need: ')
if product in products:
    quantity = int(input('How many?: '))
price = products[product]
print(f'To pay: {quantity * price }')
if product not in products:
    print('Wrong choice, choose corectly!')
    quit()







