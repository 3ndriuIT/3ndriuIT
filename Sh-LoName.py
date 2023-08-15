# From list show shortest and longest name.

names = ['karolina', 'andzelina', 'wladyslaw', 'marek', 'konrad', 'mariusz', 'maks']
shortest_name = None
longest_name = None

for name in names:
    if shortest_name is None or len(name) < len(shortest_name):
        shortest_name = name
    if longest_name is None or len(name) > len(longest_name):
        longest_name = name

print(f'longest name is: {longest_name}')
print(f'shortest name is: {shortest_name}')
