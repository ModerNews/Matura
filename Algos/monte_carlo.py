from random import randint

a = 0
pi = 10

num = 10000
ar = []


def f(x):
    return 10 * x + 10 * x^2 + 35


integral = 0.0


for i in range(num):
    integral += f(randint(0, pi))

ans = (pi-a)/float(num)*integral
print(ans)