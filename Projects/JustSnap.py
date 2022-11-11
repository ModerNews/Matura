from random import randint, choice, choices

filename = input('Filename: ')
with open(filename, encoding='utf-8') as file:
    data = file.read()

print(data)
print()

snapped_text = choices(data, k=int(len(data)/2))

with open(filename, 'w', encoding='utf-8') as file:
    file.write(''.join(snapped_text))
