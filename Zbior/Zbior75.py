#75.1
tekst = open("res/75/tekst.txt").read().split(" ")

cipherCode = {}
j = 0
for i in range(97, 123):
    cipherCode[chr(i)] = j
    j += 1

print("\n75.1")
for word in tekst:
    if word[0] == 'd':
        tempLetter = word[-1]
        if tempLetter == 'd':
            print(word)


def cipher(word, key):
    retWord = []
    for letter in word:
        code = cipherCode[letter]
        code = code * key[0] + key[1]
        if code > 25:
            code = code % 26
        retWord.append(list(cipherCode.keys())[list(cipherCode.values()).index(code)])
    return "".join(retWord)


print("\n75.2")
for word in tekst:
    if len(word) >= 10:
        print(cipher(word, [5, 2]))

print("\n75.3")
file = open("res/75/probka.txt").read().split("\n")

num = 0
for line in file[:-1]:
    num += 1
    words = line.split(" ")
    for i in range(1, 26):
        for j in range(26):
            ciphered = cipher(words[0], [i, j])
            if ciphered == words[1]:
                print("szyfrujący " + str(num) + ": (" + str(i) + ", " + str(j) + ")")
                break
    for i in range(1, 26):
        for j in range(26):
            ciphered = cipher(words[1], [i, j])
            if ciphered == words[0]:
                print("deszyfrujący " + str(num) + ": (" + str(i) + ", " + str(j) + ")")
                break