def to_pseudo_json(file):
    list = []
    temp = file.read().split('\n')
    temp[0] = temp[0].split('\t')
    for line in temp[1:-1]:
        line = line.split('\t')
        temp_dict = {}
        i = 0
        for element in line:
            temp_dict[temp[0][i]] = element
            i += 1
        list.append(temp_dict)
    return list


meldunek = []
studenci = []
wypozyczenia = []

with open('meldunek.txt') as file:
    meldunek = to_pseudo_json(file)

with open('wypozyczenia.txt') as file:
    wypozyczenia = to_pseudo_json(file)

with open('studenci.txt') as file:
    studenci = to_pseudo_json(file)

print(meldunek)
print(studenci)
print(wypozyczenia)

returns = {}
books = {}

for element in wypozyczenia:
    if element['pesel'] in list(returns.keys()):
        returns[element['pesel']] += 1
        books[element['pesel']].append(element['tytul'])
    else:
        returns[element['pesel']] = 1
        books[element['pesel']] = [element['tytul']]

print('#5.1')
index = 0
max_pesel = str(list(returns.keys())[list(returns.values()).index(max(list(returns.values())))])
print(max_pesel)
for elem in studenci:
    if elem['pesel'] == max_pesel:
        index = studenci.index(elem)
print(studenci[index]['imie'], studenci[index]['nazwisko'], books[max_pesel])

returns.clear()

returns = []
in_town = []
rooms = {}
k = 0
n = 0
print('#5.2')
for element in meldunek:
    n += 1
    in_town.append(element['pesel'])
    if not element['id_pok'] in returns:
        returns.append(element['id_pok'])
        k += 1
    if element['id_pok'] in list(rooms.keys()):
        rooms[element['id_pok']].append(element['pesel'])
    else:
        rooms[element['id_pok']] = [element['pesel']]

print(round(n / k, 4))

print('#5.3')
m = 0
w = 0
for element in studenci:
    if int(element['pesel'][-2]) % 2 == 0:
        w += 1
    else:
        m += 1

print(f'Mężczyzn: {m}\nKobiet: {w}')

print('#5.4')
returns.clear()
temp = []
for element in studenci:
    if not element['pesel'] in in_town:
        temp.append(element['pesel'])

returns = []
for element in studenci:
    if element['pesel'] in temp:
        returns.append(f'{element["nazwisko"]} {element["imie"]}')

returns = sorted(returns)
print(returns)

print('#5.5')
# print(rooms)
# rooms = dict(sorted(rooms.items()))
books_per_room = {}
for element in wypozyczenia:
    for room in rooms:
        if element['pesel'] in rooms[room]:
            if room in list(books_per_room.keys()):
                books_per_room[room].append(element['tytul'])
            else:
                books_per_room[room] = [element['tytul']]

n = 0
print(rooms)
books_per_room = dict(sorted(books_per_room.items()))
for element in books_per_room:
    k = len(books_per_room[element]) - len(set(books_per_room[element]))
    n += k
    print(element, k)

print(len(wypozyczenia) - n)