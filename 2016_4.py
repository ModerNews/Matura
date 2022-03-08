import datetime

start = 0
end = 1500

capacity = 5000  # 5 litres
max_capacity = 5000
percentage = 0.80

current = start + 1

added = 0
ans_3 = [["Dzien", "Roztwor X", "Woda"]]

while True:
    chem = capacity * percentage
    water = capacity * (1 - percentage)
    ans_3.append([str(current - 1), str(round(chem, 2)), str(round(water, 2))])
    if current > end:
        break

    if current == 191:
        chem = capacity * percentage
        water = capacity * (1 - percentage)
        ans_1 = [capacity, round(chem, 2), round(water, 2)]

    if current % 2 == 0:
        capacity -= 20

    if (current - 51) % 50 == 0:
        chem = capacity * percentage
        water = capacity * (1 - percentage) + (max_capacity - capacity)
        added += max_capacity - capacity
        capacity = max_capacity
        percentage = chem/capacity

    current += 1


print("#1\n", ans_1)
print("#2\n", round(percentage * 100, 2), added)
with open("chemia.csv", 'a'):
    pass

with open("chemia.csv", "w") as file:
        file.write("\n".join([", ".join(line) for line in ans_3]))

print("#3\n", "Output written to chemia.csv\nPlot in chemia.xlsx")
print("#4\n", "28.04, for more refer to 2016_4_brute.py")