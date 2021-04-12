with open('galerie.txt') as file:
    data = file.read()

data = data.split('\n')
parsed = []
for n in data[:-1]:
    n = n.split(' ')
    y = {'country': n[0],
         'town': n[1],
         'locals': n[2:],
         'locals_sizes': None,
         'total': 0}
    parsed.append(y)

countries = {}
for data in parsed:
    if data['country'] in list(countries.keys()):
        countries[data['country']] += 1
    else:
        countries[data['country']] = 1

print('#4.1')
for i in range(len(countries)):
    print(f'{list(countries.keys())[i]}: {list(countries.values())[i]}')

print('\n#4.2')
n = len(parsed[0]['locals']) / 2
floors = []
for mall in parsed:
    temp1 = []
    for i in range(int(n)):
        temp1.append(int(mall['locals'][i*2]) * int(mall['locals'][i*2 + 1]))
    parsed[parsed.index(mall)]['locals'] = [int(i) for i in mall['locals'] if int(i) != 0]
    parsed[parsed.index(mall)]['total'] = sum(temp1)
    parsed[parsed.index(mall)]['locals_sizes'] = [int(i) for i in temp1 if int(i) != 0]
    floors.append(sum(temp1))
    print(mall['town'] + ' ' + str(parsed[parsed.index(mall)]['total']) + ' ' + str(int(len(parsed[parsed.index(mall)]['locals']) / 2)))

town = 'town'
print(f'\nMax: {parsed[floors.index(max(floors))][town]} {max(floors)}')
print(f'Min: {parsed[floors.index(min(floors))][town]} {min(floors)}')

print('\n#4.3')
uniques = []
for mall in parsed:
    uniques.append(len(set(mall['locals_sizes'])))

print(f'Max: {parsed[uniques.index(max(uniques))][town]} {max(uniques)}')
print(f'Min: {parsed[uniques.index(min(uniques))][town]} {min(uniques)}')