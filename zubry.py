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

First = None

while True:
    if now in key_dates:
        key_dates_values[str(now.date())] = {'siano': wheat/1000, 'żołędzie': acorns/1000}

    print(now, wheat, acorns)

    if wheat >= 50000:
        count_only_wheat += 1
        wheat -= 40*animals
    else:
        if not First:
            First = now
        count_only_acorns += 1
        acorns -= 20*animals

    if now.weekday() == 5:
        count_wheat += 1
        wheat += 15000
    if now.weekday() == 2:
        count_acorns += 1
        acorns += 4000

    now += datetime.timedelta(days=1)

    if now > end:
        break

print("#1\n", "Siano:", count_wheat, "\n", "Żołędzie:", count_acorns)
print("#2\n", First.date())
print("#3\n", "Tylko siano:", count_only_wheat, "\n", "Tylko żołędzie:", count_only_acorns)
print("#4\n", key_dates_values)

out_str = [' , ' + ', '.join(key_dates_values.keys()),
           'Żołędzie: , ' + ', '.join([str(day['żołędzie']) for day in key_dates_values.values()]),
           'Siano: , ' + ', '.join([str(day['siano']) for day in key_dates_values.values()])]
with open('zubry_out.csv', 'a'):
    pass
with open('zubry_out.csv', 'w', encoding='utf-8') as file:
    file.write('\n'.join(out_str))
print('Written to zubry_out.csv')

print("#5\n", '121, for more refer to zubry_brute.py')
