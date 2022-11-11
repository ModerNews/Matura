data = [1, -2, 6, -5, 7, -3]

sums = []

for i in range(len(data) - 1):
    for j in range(len(data))[i:]:
        if j != len(data):
            sums.append(sum(data[i:j]))
        else:
            sums.append(sum(data[i:]))

with open('DANE/dane5-1.txt') as file:
    data = file.read().split('\n')

for i in range(len(data) - 1):
    data[i] = int(data[i])

print(max(sums))

sums = []

for i in range(len(data) - 1):
    for j in range(len(data))[i:]:
        if j != len(data):
            sums.append(sum(data[i:j]))
        else:
            sums.append(sum(data[i:]))

print(max(sums))
