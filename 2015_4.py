with open("liczby.txt", 'r+') as file:
    data = file.read().split("\n")

def count_chars(word: str) -> list[int]:
    return [word.count("0"), word.count('1')]

print('#1')
more_0: list[str] = []
for word in data:
    temp = count_chars(word)
    if temp[0] > temp[1]:
        more_0.append(word)

print(len(more_0))

converted_numbers: list[int] = []
for word in data:
    exec(f"converted_numbers.append(int(0b{word}))")

by_2 = 0
by_8 = 0
for number in converted_numbers:
    if number % 2 == 0:
        by_2 += 1
    if number % 8 == 0:
        by_8 += 1

print("#2")
print(by_2, by_8)

print("#3")
print(converted_numbers.index(max(converted_numbers)) + 1, converted_numbers.index(min(converted_numbers)) + 1)