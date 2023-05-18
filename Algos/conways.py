from copy import deepcopy

start_set = "xxxxxxxxxx\n" \
            "xxxxxoxoxo\n" \
            "xxooxxoxoo\n" \
            "xoooxxoxxo\n" \
            "xxxxxxxxxx"

data = [list(line) for line in start_set.split('\n')]
print(data)

generations = [data]

for i in range(100):
    new_gen = deepcopy(generations[-1])
    for x in range(len(data[0])):
        for y in range(len(data)):
            neighbors = [data[y-1][x-1], data[y-1][x], data[y][x+1 % len(data[0])],
                         data[y][x-1], data[y][x+1 % len(data[0])],
                         data[y+1 % len(data)][x-1], data[y+1 % len(data)][x], data[y+1 % len(data)][x+1 % len(data[0])]]
            if neighbors.count('o') < 2:
                new_gen[x][y] = 'x'
            elif data[x][y] == 'o' and (2 <= neighbors.count('o') <= 3):
                new_gen[x][y] = 'o'
            elif data[x][y] == 'x' and neighbors.count('o') == 3:
                new_gen[x][y] = 'o'
            else:
                new_gen[x][y] = 'x'
    generations.append(deepcopy(new_gen))

print(generations)
