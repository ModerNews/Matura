import datetime

onetime = 26
appended = 300

add = False
always = False

while True:
    start = datetime.datetime(day=15, month=9, year=2015)
    end = datetime.datetime(day=31, month=3, year=2016)
    temp = start

    storage = 550
    appended += 1
    helper = True
    while helper:
        # morning
        print(temp.date(), temp.weekday(), 'mrn', storage)
        if storage < 100 and temp.weekday() == 4:
            add = True

        if temp.weekday() in (5, 6) and storage > onetime:
            storage -= onetime
        else:
            if temp.weekday() in (5, 6) and storage < onetime:
                helper = False

        # midday
        if add:
            storage += appended
            add = False

        # evening
        print(temp.date(), temp.weekday(), 'evn', storage)
        if storage > onetime:
            storage -= onetime
        else:
            helper = False
        temp += datetime.timedelta(days=1)
        if temp > end:
            break
    if helper is True:
        break

print(appended)