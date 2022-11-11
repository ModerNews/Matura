import datetime

animals = 90
start = datetime.datetime(day=1, month=12, year=2012)
end = datetime.datetime(day=28, month=2, year=2013)

wheat = 100000  # 100t = 100000 kg
acorns = 5000  # 5t = 5000 kg

now = start

count_wheat = 0
count_acorns = 0
count_only_wheat = 0
count_only_acorns = 0
key_dates = [datetime.datetime(day=31, month=12, year=2012), datetime.datetime(day=31, month=1, year=2013), datetime.datetime(day=28, month=2, year=2013)]
key_dates_values = {}

dead = False

First = None
while not dead:
    animals += 1
    wheat = 100000  # 100t = 100000 kg
    acorns = 5000  # 5t = 5000 kg
    start = datetime.datetime(day=1, month=12, year=2012)
    now = start
    end = datetime.datetime(day=28, month=2, year=2013)
    while True:
        if now in key_dates:
            key_dates_values[str(now.date())] = {'siano': wheat / 1000, 'żołędzie': acorns / 1000}

        print(now, wheat, acorns)

        if wheat >= 50000:
            count_only_wheat += 1
            wheat -= 40 * animals
        else:
            if not First:
                First = now
            count_only_acorns += 1
            acorns -= 20 * animals
            if acorns < 0:
                dead = True
                break

        if now.weekday() == 4:
            count_wheat += 1
            wheat += 15000
        if now.weekday() == 1:
            count_acorns += 1
            acorns += 4000

        now += datetime.timedelta(days=1)

        if now > end:
            break

print(animals)