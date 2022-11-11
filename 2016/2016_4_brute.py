import datetime

change = 20.00

while True:
    start = 0
    end = 1500

    capacity = 5000  # 5 litres
    max_capacity = 5000
    percentage = 0.80

    current = start + 1

    added = 0
    ans_3 = [["Dzien", "Roztwor X", "Woda"]]

    change += 0.01
    finished = False

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
            capacity -= change

        if (current - 51) % 50 == 0:
            chem = capacity * percentage
            water = capacity * (1 - percentage) + (max_capacity - capacity)
            added += max_capacity - capacity
            capacity = max_capacity
            percentage = chem/capacity
            if percentage < 0.01:
                finished = True

        current += 1

    if finished:
        print(change)
        break