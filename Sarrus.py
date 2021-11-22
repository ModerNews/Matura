import math

filepath = "res\\Sarrus.txt"

with open(filepath, "r+") as file:
    matrix: list[str] = file.read().split("\n")

for i in range(len(matrix)):
    matrix[i]: list[list[str]] = matrix[i].split(', ')
    for n in range(len(matrix[i])):
        matrix[i][n] = int(matrix[i][n])

matrix: list[list[int]]  # 2 dimensional array, read from file, after parsing

for i in range(len(matrix) - 1):
    matrix.append(matrix[i])

sum_r = 0

for i in range(len(matrix) - 2):
    temp = [matrix[j + i][j] for j in range(len(matrix[0]))]
    temp2 = temp[0]
    for j in range(len(temp) - 1):
        temp2 = temp2 * temp[j + 1]
    sum_r += temp2

sum_b = 0

for i in range(len(matrix) - 2):
    temp = [matrix[j + i][-(j + 1)] for j in range(len(matrix[0]))]
    temp2 = temp[0]
    for j in range(len(temp) - 1):
        temp2 = temp2 * temp[j + 1]
    sum_b += temp2

print("Macierz:")
for i in range(len(matrix[math.floor(len(matrix)/2)])):
    if i == 0:
        print(f'\u250C {str(matrix[i]).replace("[", "").replace("]", "")} \u2510')
    elif i == len(matrix[math.floor(len(matrix)/2)]) - 1:
        print(f'\u2514 {str(matrix[i]).replace("[", "").replace("]", "")} \u2518')
    else:
        print(f'\u2502 {str(matrix[i]).replace("[", "").replace("]", "")} \u2502')

print(f"\nWyznacznik:\n{sum_r - sum_b}")