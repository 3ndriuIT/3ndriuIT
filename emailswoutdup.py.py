
#Odbierz od uzytkownika 10 adresow email i wyswietl je ponizej bez duplikatów

emails = set()

for _ in range(10):
    emails.add(input('podaj adres email: '))

print(emails)
