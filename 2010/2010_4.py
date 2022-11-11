with open('anagram.txt', 'r') as file:
    data = file.read().split('\n')

same_length_lines = []
anagram_lines = []

for line in data:
    words = line.split(' ')
    first_length = len(words[0])
    if all(len(temp) == first_length for temp in words[1:]):
        same_length_lines.append(words)

for line in same_length_lines:
    first_word = line[0]
    anagram = True
    for word in line[1:]:
        if not all(char in word for char in first_word):
            anagram = False

    if anagram:
        anagram_lines.append(line)

print('#1\n', same_length_lines)
with open('odp4a.txt', 'a'):
    pass
with open('odp4a.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(" ".join(line) for line in same_length_lines))

print('#2\n', anagram_lines)
with open('odp4b.txt', 'a'):
    pass
with open('odp4b.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(" ".join(line) for line in anagram_lines))