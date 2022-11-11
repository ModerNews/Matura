import math

ex: str  # dokładność pierwiastka
ey: str  # dokładność funkcji
a: str  # przedział funkcji niższy
b: str  # przedział funkcji wyższy
f: str  # funkcja

__symbols__ = {"^": "**",
               "sin(": "math.sin(",
               "cos(": "math.cos(",}

a = input("Provide a... ")
b = input("Provide b... ")
ex = input("Provide εx... ")
ey = input("Provide εy... ")
f = input("Provide function...\n")

f_dec: str = f  # decorative form of function (to print)

# replace operation symbols
for k in list(__symbols__.keys()):
    f = f.replace(k, __symbols__[k])
    ex = ex.replace(k, __symbols__[k])
    ey = ey.replace(k, __symbols__[k])
    a = a.replace(k, __symbols__[k])
    b = b.replace(k, __symbols__[k])

# calculate values of variable
ex: float = float(eval(ex))
ey: float = float(eval(ey))
a: float = float(eval(a))
b: float = float(eval(b))

# present information
print("Data:")
print(f"\tRange verge a: {a}")
print(f"\tRange verge b: {b}")
print(f"\tRoot uncertainty εx: {ex}")
print(f"\tFunction uncertainty εy: {ey}")
print(f'\nFunction:\n{f_dec}')


value1 = eval(f.replace("x", f"({a})"))
value2 = eval(f.replace("x", f"({b})"))

if value1 * value2 > 0:
    raise ValueError("Funkcja od 'a' i funkcja od 'b' muszą mieć różne znaki")

while True:
    value3 = None
    avg = (a + b)/2

    if abs(a - avg) < ex:
        print(avg)
        quit()

    value3 = eval(f.replace("x", f"({avg})"))

    if abs(value3) < ey:
        print(avg)
        quit()

    if value3 * value1 < 0:
        b = avg
    else:
        a = avg
        value1 = value3
