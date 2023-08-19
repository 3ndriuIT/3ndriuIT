# Policz ile razy w zadniu: .. wystapiło slowo 'pies'
#
# Dwa sposoby:

sentence = 'Pies to najlepszy przyjaciel czlowieka, lecz nie kazdy pies o tym wie'
sentence = sentence.lower()
print(sentence)
print(sentence.count('pies'))

word_pies = 0

for letter in sentence.split(' '):
    if letter == 'pies':
        word_pies += 1

print(word_pies)
