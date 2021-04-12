import math
file = open("res/73/tekst.txt").read()

data1 = file.split(" ")
ans = 0

#73.1
for word in data1:
    ind = 0
    for letter in word:
        try:
            if ord(letter) == ord(word[ind + 1]):
                ans += 1
                break
            ind += 1
        except IndexError:
            break

print("Słowa z dwoma identycznymi literami pod rząd" + str(ans))

#73.2
spaces = file.count(" ")
letters = len(file) - 1
letters = letters - spaces
for i in range(65, 91):
    count = file.count(chr(i))
    percentage = str(count / letters * 100) + "%"
    print(str(chr(i)) + ": " + str(count) + "(" + str(percentage) +")")

def vowel_checker(word):
    curr = 0
    subword = 0
    for letter in word.lower():
        if letter == "a" or letter == "o" or letter == "e" or letter == "i" or letter == "u" or letter == "y":
            curr = 0
        else:
            curr += 1
        if curr > subword:
            subword = curr
    return subword


#73.3
longest = 0
counter = 0
for word1 in data1:
    word1 = word1.lower()
    if vowel_checker(word1) > longest:
        counter = 1
        longest = vowel_checker(word1)
        ans = word1
    elif vowel_checker(word1) == longest:
        counter += 1

print("Najwięcej spółgłosek pod rząd" + str(longest))
print("Słowa z takim podsłowem" + str(counter))
print("Pierwsze z nich" + str(ans))