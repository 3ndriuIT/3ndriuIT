# Pokaz wspolne wspolne liczby oraz ich ilosc dla 3 i 5
# w zbiorze liczb od 0 do 1000

divisible_by_3 = 0
divisible_by_5 = 0

liczby3 = set(range(0, 1001, 3))
liczby5 = set(range(0, 1001, 5))

print(sorted(liczby3 & liczby5)) # lista wspolnych liczb

liczby = list(range(0, 1001,))

for liczba in liczby:
    if liczba % 3 == 0:
        divisible_by_3 += 1
    if liczba % 5 == 0:
        divisible_by_5 += 1

print(divisible_by_3 & divisible_by_5) # ilosc wspolnych liczb
