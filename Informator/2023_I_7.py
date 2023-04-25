import copy

with open('DANE/szyfrogram.txt', 'r') as file:
    data = file.read()

count = {}
for char in range(ord('A'), ord('Z')+1):
    char = chr(char)
    if char not in count.keys():
        count[char] = data.count(char)

print('#7.1\n' + '\n'.join([f'{key} {value}' for key, value in sorted(count.items())]))

# W 7.2 dane litery odpowiadają sobie, jeśli ich częstotliwości wystąpień są takie same, np.:
# A w szyfrogramie występuje 41 razy, w uśrednionym tekście 41 razy występuje litera L, stąd A=L
# Zaszyfrowane słowo to: **Algorytm**

# 7.3 polega na tym samym na większą skalę:

with open('DANE/czestosc.txt', 'r') as file:
    # Tu one-liner, bo mi się nudziło, nie polecam do używania na codzień
    # decyphered = [[1 if (data := data.replace(key, coding[str(value)].lower())) else 0 for key, value in count.items() if value != 0] for i in range(1) if (coding := {params[1]: params[0] for line in file.read().split('\n')[:-1] if (params := line.split(' ')) and params[1] != '0'})]
    key = {params[1]: params[0] for line in file.read().split('\n')[:-1] if (params := line.split(' ')) and params[1] != '0'}

decyphered = copy.copy(data)

for char, counter in count.items():
    if counter != 0:
        decyphered = decyphered.replace(char, key[str(counter)].lower())

# W rozwiązaniu do 7.3 jest błąd - znaki, które powine być U zostały oznaczone jako B
print('#7.3\n' + decyphered.upper())
# print('#7.3\n' + data.upper())