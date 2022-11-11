def step(string: list[str], instruction: str, value: str):
    value = value.title()
    if instruction.lower() == 'dopisz':
        string.append(value)
    elif instruction.lower() == 'zmien':
        string[-1] = value
    elif instruction.lower() == 'usun':
        string = string[:-1]
    elif instruction.lower() == 'przesun':
        index = string.index(value)
        string[index] = chr(ord(string[index]) + 1) if string[index] != 'Z' else 'A'

    return string

string = []

with open('../instrukcje.txt', 'r') as file:
    instructions = file.read()

instructions = instructions.split('\n')[:-1]

for instruction in instructions:
    instruction = instruction.split(' ')

    string = step(string, instruction[0], instruction[1])
    print(string)

print('#1')
print(len(string))

print('#2')
last_instruction = ''
temp = 1
len = 0
for instruction in instructions:
    instruction = instruction.split(' ')[0]
    if instruction == last_instruction:
        temp += 1
    else:
        if len < temp:
            len = temp
        temp = 1
        last_instruction = instruction
print(len)

print('#3')
letters = {}
for instruction in instructions:
    instruction = instruction.split(' ')
    if instruction[0].lower() == "dopisz":
        if instruction[1] in letters:
            letters[instruction[1]] += 1
        else:
            letters[instruction[1]] = 1

print(letters)
print(list(letters.keys())[list(letters.values()).index(max(list(letters.values())))])

print('#4')
print(''.join(string))
