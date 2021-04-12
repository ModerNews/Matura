def encryption(text, key):
    sumkey = key
    iCounter = 1
    while len(key) <= len(text.replace(" ","").replace(",","").replace(".","").replace("!","").replace("?","")):
        var1 = len(key)
        var2 = len(text.replace(" ","").replace(",","").replace(".","").replace("!","").replace("?",""))
        key = key + sumkey
        iCounter += 1
    encrypted = []
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            temp1 = ord(text[i])
            temp2 =ord(key[counter])
            temp = (temp1 + temp2) % 26 + 65
            encrypted.append(chr(temp))
            counter += 1
        else:
            encrypted.append(text[i])
    return "".join(encrypted), iCounter

def decryption(text,key):
    sumkey = key
    while len(key) <= len(text):
        key = key + sumkey
    decrypted = []
    counter = 0
    for i in range(len(text)):
        if text[i].isalpha():
            temp1 = ord(text[i])
            temp2 = ord(key[counter])
            temp = (temp1 - temp2) % 26 + 65
            decrypted.append(chr(temp))
            counter += 1
        else:
            decrypted.append(text[i])
    return "".join(decrypted)

print("77.1")
file = open("res/77/dokad.txt").read()
temp = encryption(file, "LUBIMYCZYTAC")
print("powtórzenia: " + str(temp[1]))
print(temp[0])

print("\n77.2")
file2 = open("res/77/szyfr.txt").read().split("\n")
print(decryption(file2[0], file2[1]))

print("\n77.3")
characters = {}
temp = 0
n = 0
for i in range(65, 91):
    counted = file2[0].count(chr(i))
    characters[chr(i)] = counted
    print(chr(i) + ": " + str(counted))
    n += counted
    temp += counted * (counted - 1)

k = (temp / (n * (n-1)))
length = str(round(0.0285 / (k - 0.0385), 3))
print("Szacowana długość: " + length)
print("Faktyczna długość: " + str(len(file2[1])))
