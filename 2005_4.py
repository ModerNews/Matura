import math


def F(N):
    m = (0.0001 * N)
    return 10 * m ** 3 + 7 * m ** 2 + 0.1 * m + 0.1

D_1 = []
D_2 = []

print("#1")
lines = [["N", "Koszt D1", "Koszt D2"]]
for N in range(1, 7001):
    D_1_cost = round(0.01 * N + F(N), 2)
    D_2_cost = round(0.5 * math.sqrt(N) + 5 * F(N), 2)
    if D_1_cost < D_2_cost:
        D_1.append(N)
    else:
        D_2.append(N)
    if N in (100, 1000, 5000):
        lines.append[N, D_1_cost, D_2_cost]

with open('2005_4.csv', 'a'):
    pass

with open('2005_4.csv', 'a') as file:
    file.write(f'Wybierz D_1 w: , ')

with open('2005_4.csv', 'a') as file:
    file.write("\n".join([', '.join(line) for line in lines]))

print(D_1)
print(D_2)

print("#2")
lines = [['N', 'Koszt obliczeń', 'Koszt licencji']]
for N in range(6000, 9001, 100):
    license_cost = round(0.5 * math.sqrt(N), 2)
    cost = round(5 * F(N), 2)
    lines.append([N, cost, license_cost])

with open('2005_4.csv', 'a'):
    pass

with open('2005_4.csv', 'a') as file:
    file.write("\n".join([', '.join(line) for line in lines]))

print("Written table to 2005_4.csv")
