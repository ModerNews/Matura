with open("slowa.txt") as file:
    data = file.read().split("\n")

final = []
for word in data:
    final.append(word[::-1])

open("hasła_a.txt", "w").close()
with open('hasła_a.txt', 'a') as file:
    for word in final:
        print(word, file=file)

def findPalindrome(text):
    for i in range(len(text), -1, -1):
        temp1 = text[:i][::-1]
        temp2 = text[:i]
        if temp1 == temp2:
            temp3 = text[::-1][:-i]
            return temp3

print("#1")
for word in final:
    if len(word) >= 12:
        print(findPalindrome(word) + word)
print('#2')
maxLen = 0
ind = 0
for word in final:
    if len(word) > maxLen:
        maxLen = len(word)
        ind = final.index(word)