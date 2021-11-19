import math

ex: str  # dokładność pierwiastka
n: str  # liczba aproksymacji
a: str  # przedział funkcji niższy
b: str  # przedział funkcji wyższy
f: str  # funkcja

__symbols__ = {"^": "**",
               "sin(": "math.sin(",
               "cos(": "math.cos(",}

a = input("Provide a... ")
b = input("Provide b... ")
ex = input("Provide εx... ")
n = input("Provide n... ")
f = input("Provide function...\n")

f_dec: str = f  # decorative form of function (to print)

# replace operation symbols
for k in list(__symbols__.keys()):
    f = f.replace(k, __symbols__[k])
    ex = ex.replace(k, __symbols__[k])
    n = n.replace(k, __symbols__[k])
    a = a.replace(k, __symbols__[k])
    b = b.replace(k, __symbols__[k])

# calculate values of variable
ex: float = float(eval(ex))
n: float = float(eval(n))
a: float = float(eval(a))
b: float = float(eval(b))

value1 = eval(f.replace("x", f"({a})"))
value2 = eval(f.replace("x", f"({b})"))

if value1 * value2 > 0:
    raise ValueError("Funkcja od 'a' i funkcja od 'b' muszą mieć różne znaki")

while True:
    start_x = (value1 * b - value2 * a)/(value1 - value2)
    if n == 0:
        print(start_x)
        break
    else:
        n -= 1
    value4 = float(eval(f.replace("x", f"({start_x})")))
    if abs(value4) < ex:
        print("Data:")
        print(f"\tRange verge a: {a}")
        print(f"\tRange verge b: {b}")
        print(f"\tRoot uncertainty εx: {ex}")
        print(f"\tFunction uncertainty n: {n}")
        print(f'\nFunction:\n{f_dec}')
        print(f"\nAns.: {start_x}")
        quit()

    if value4 * value1 < 0:
        b = start_x
        value2 = value4
    else:
        a = start_x
        value1 = value4

