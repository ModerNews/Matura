print("Encrypted words\n\n")
words = open("tj.txt").read().split("\n")
keys = open("klucze1.txt").read().split("\n")
code = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

for word in words:
    key = keys[words.index(word)]
    sumkey = key
    while len(key) < len(word):
        key = key + sumkey

    for i in range(len(word)):
        temp = ord(word[i]) + code[key[i]]
        if temp > 90:
            temp = temp - 26
        word = word[:i] + chr(temp) + word[i + 1:]

    print(word)

print("\nDecrypted Words\n\n")
words = open("sz.txt").read().split("\n")
keys = open("klucze2.txt").read().split("\n")

for word in words:
    key = keys[words.index(word)]
    sumkey = key
    while len(key) < len(word):
        key = key + sumkey

    for i in range(len(word)):
        temp = ord(word[i]) - code[key[i]]
        if temp < 65:
            temp = temp + 26
        word = word[:i] + chr(temp) + word[i + 1:]

    print(word)