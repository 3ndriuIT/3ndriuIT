# Napisz program zliczający ilość wystąpień każdego znaku w zadanym napisie !


sentence = (input('Napisz cos, a ja podlicze ilosc kazdego znaku: '))
sentence = sentence.replace(' ', '')

# znaki[:] = count # TZW. LIST SLICING !!
# print(znaki)

marks = []

for letter in sentence:
    if letter in sentence:
        marks += letter

counted = {}

for value in marks:
    counted[value] = marks.count(value)
print(counted)
