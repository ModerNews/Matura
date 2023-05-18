from copy import deepcopy

start_set = "xxxxxxxxxx\n" \
            "xxxxxoxoxo\n" \
            "xxooxxoxoo\n" \
            "xoooxxoxxo\n" \
            "xxxxxxxxxx"

generations = [[list(line) for line in start_set.split('\n')]]

for i in range(100):
    new_gen, data = deepcopy(generations[-1]), generations[-1]
    for x in range(len(data[0])):
        for y in range(len(data)):
            neighbors = [data[y-1][x-1], data[y-1][x], data[y-1][(x+1) % len(data[0])],
                         data[y][x-1], data[y][(x+1) % len(data[0])],
                         data[(y+1) % len(data)][x-1], data[(y+1) % len(data)][x], data[(y+1) % len(data)][(x+1) % len(data[0])]]
            if neighbors.count('o') < 2:
                new_gen[y][x] = 'x'
            elif data[y][x] == 'o' and (2 <= neighbors.count('o') <= 3):
                new_gen[y][x] = 'o'
            elif data[y][x] == 'x' and neighbors.count('o') == 3:
                new_gen[y][x] = 'o'
            else:
                new_gen[y][x] = 'x'
    generations.append(deepcopy(new_gen))

i = 1
for gen in generations:
    print(f"Generation: {i}")
    print('\n'.join([' '.join(line) for line in gen]))
    i += 1