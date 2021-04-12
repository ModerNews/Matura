file = open("res\\2012\\74\\pp\\cyfry.txt").read().split("\n")

counter = 0
for number in file[:-1]:
    if int(number) % 2 == 0:
        counter += 1

print("a) \n" + str(counter))

largest = 0
largestAns = ""
smallest = 25700000
smallestAns = ""
for number in file[:-1]:
    temp = 0
    for n in number:
        temp += int(n)
    if temp > largest:
        largest = temp
        largestAns = number
    elif temp < smallest:
        smallest = temp
        smallestAns = number

print("b)")
print(largestAns)
print(smallestAns)
print("c)")
for number in file[:-1]:
    temp = 0
    tempLen = 0
    for n in number:
        if int(n) > temp:
            temp = int(n)
            tempLen += 1
        else:
            break
    if tempLen == len(number):
        print(number)