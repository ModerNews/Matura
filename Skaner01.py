filepath = "res\\Skaner01.txt"

with open(filepath, "r+") as file:
    matrix: list[str] = file.read().split("\n")

for i in range(len(matrix)):
    matrix[i]: list[list[str]] = matrix[i].split(', ')
    for n in range(len(matrix[i])):
        matrix[i][n] = int(matrix[i][n])

matrix: list[list[int]]  # 2 dimensional array, read from file, after parsing
returns: list[int] = []

# returns = [0 for n in range(len(matrix)) for i in range(len(matrix[0]))]


returns = [eval(str(line).replace("[", "").replace("]", "").replace(", ", " + ")) for line in [[matrix[n][i] for n in range(len(matrix))] for i in range(len(matrix[0]))]]

print(returns)