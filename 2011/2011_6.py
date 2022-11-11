with open("2011_res\\liczby.txt", "r") as file:
    data = file.read().split("\n")[:-1]

even = sum([1 if line[-1] == '0' else 0 for line in data])
print("#1\n", even)

int_data = []
for line in data:
    int_data.append(int(line, 2))

print("#2\n", max(int_data), data[int_data.index(max(int_data))])

print('#3\n', bin(sum([0 if len(line) != 9 else int(line, 2) for line in data]))[2:])
