with open("dane_medale.txt") as file:
    data = {tmp[0]: [int(obj) if len(obj) < 4 else obj for obj in tmp[1:]] for line in file.read().split('\n')[1:-1] if (tmp := line.split('\t'))}

print(data)

print('#92.1')
print(len(countries := [k for k, v in data.items() if v[1] >= 1 and v[5] >= 1 and (sum(v[2:5]) >= 1 and sum(v[6:]) == 0)]))
print(sum([sum(data[country][2:5]) for country in countries]))

print('#92.2')
continents = {'continent': ['OL_Letnie', 'OL_Zimowe']}
for country, params in data.items():
    if params[0] in continents.keys():
        continents[params[0]][0] += params[1]
        continents[params[0]][1] += params[5]
    else:
        continents[params[0]] = [params[1], params[5]]

print('#5.2')
print('Output has been written to Zbior92.5.csv')

with open('Zbior92.5.csv', 'w') as file:
    file.write('\n'.join(['\t'.join([continent] + [str(points[0]), str(points[1])]) for continent, points in continents.items()]))