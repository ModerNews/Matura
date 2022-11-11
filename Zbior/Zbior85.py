import datetime
import math

start_day = datetime.datetime(2014, 4, 23, 0, 0, 0)
current_day = datetime.datetime(2014, 4, 23, 0, 0, 0)
end_day = datetime.datetime(2014, 9, 29, 0, 0, 0)
change_day = datetime.datetime(2014, 6, 24, 0, 0, 0)
shoping_start = datetime.datetime(2014, 4, 29, 0, 0, 0)

animals = 600
milk_daily = 0.5
milk = 0

change = 1.04

cheese_storage = []
finished_cheese = 0
cheese_sold = {}
mixes = {"owcze": 0,
         "krowie 20%": 0,
         "krowie 40%": 0}

tried_to_buy = 0
buyed = 0
days_short = 0

total_milk = 0

first_day = None


def make_cheese(milk: int, modifier: float = 1.0):
    return [math.floor(milk / (6*modifier)), 6]


# def update_cheese(finished_cheese, cheese_storage):
#     for i in range(len(cheese_storage)):
#         cheese_storage[i][1] -= 1
#         if cheese_storage[i][1] == 0:
#             finished_cheese += cheese_storage[i][0]
#             cheese_storage.pop(i)
#     return finished_cheese


while True:
    if milk != 0:
        cheese_storage.append(make_cheese(milk))
        if current_day <= end_day - datetime.timedelta(5):
            mixes["owcze"] += make_cheese(milk)[0]
            mixes["krowie 20%"] += make_cheese(milk, 0.8)[0]
            mixes["krowie 40%"] += make_cheese(milk, 0.6)[0]
            print(current_day, milk, make_cheese(milk, 0.8)[0])

    if current_day > end_day:
        break
    if current_day == change_day:
        change = 0.9
    if current_day.weekday() == 2 and current_day >= datetime.datetime(2014, 4, 30, 0, 0, 0):
        milk_daily = math.round(milk_daily*change, 2)

    milk = animals * milk_daily

    for i in range(len(cheese_storage)):
        to_pop = []
        cheese_storage[i][1] -= 1
        if cheese_storage[i][1] == 0:
            finished_cheese += cheese_storage[i][0]
            to_pop.append(i)

    try:
        for i in sorted(to_pop, reverse=True):
            del finished_cheese[i]
    except NameError:
        pass

    total_milk += milk
    if current_day >= shoping_start:
        if current_day.weekday() == 5 or current_day.weekday() == 6:``
            wanted = 100
        else:
            wanted = 36

        if current_day.month not in cheese_sold.keys():
            cheese_sold[current_day.month] = 0

        tried_to_buy += wanted
        if finished_cheese >= wanted:
            buyed += wanted
            cheese_sold[current_day.month] += wanted
            finished_cheese = finished_cheese - wanted
        else:
            buyed += finished_cheese
            cheese_sold[current_day.month] += finished_cheese
            finished_cheese = 0
            days_short += 1
            if first_day is None:
                first_day = current_day
    current_day += datetime.timedelta(1)


print("#85.1", total_milk)
print("#85.2", tried_to_buy)
print("#85.3", days_short, first_day)
print("#85.4", cheese_sold)
print("#85.5", 744)
print("#85.6", mixes)


