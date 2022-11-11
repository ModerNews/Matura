def encryption(file):
    code = file[-1].split(" ")
    sumcode = code
    for line in file[:-1]:
        while len(line) > len(code):
            code = code + sumcode
        code = code[:len(line)]
        for i in range(len(line)):
            num = int(code[i])
            temp1 = line[num - 1]
            temp2 = line[i]
            line = line[:i] + temp1 + line[i + 1:]
            line = line[:num - 1] + temp2 + line[num:]
        print(line)

def decryption(file):
    code = file[-1].split(" ")
    sumcode = code
    for line in file[:-1]:
        while len(line) > len(code):
            code = code + sumcode
        code = code[:len(line)]
        for i in range(len(line) - 1, -1, -1):
            num = int(code[i])
            temp1 = line[num - 1]
            temp2 = line[i]
            line = line[:i] + temp1 + line[i + 1:]
            line = line[:num - 1] + temp2 + line[num:]
        print(line)

print("76.1")
file = open("res/76/szyfr1.txt").read().split("\n")
encryption(file)

print("\n76.2")
file2 = open("res/76/szyfr2.txt").read().split("\n")
encryption(file2)

print("\n76.3")
file3 = open("res/76/szyfr3.txt").read().split("\n")
decryption(file3)
