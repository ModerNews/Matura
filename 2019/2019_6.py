with open('dane.txt') as file:
    dane = file.read().split('\n')[:-1]

female = 0
male = 0
for pesel in dane:
    if int(pesel[9]) % 2 == 0:
        female += 1
    else:
        male += 1

print(f'#1\nKobiet: {female}\nMężczyzn: {male}')

november = 0
for pesel in dane:
    if int(pesel[2:4]) == 11 or int(pesel[2:4]) == 31:
        november += 1

print(f'#2\n{november}')

wrong_data = []
for pesel in dane:
    sum = 1 * int(pesel[0]) + 3 * int(pesel[1]) + 7 * int(pesel[2]) + 9 * int(pesel[3]) + 1 * int(pesel[4]) + 3 * int(pesel[5]) + 7 * int(pesel[6]) + 9 * int(pesel[7]) + 1 * int(pesel[8]) + 3 * int(pesel[9]) + int(pesel[10])
    if sum % 10 != 0:
        wrong_data.append(pesel)

print(f'#3\n{wrong_data}')
