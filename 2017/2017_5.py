import datetime
from calendar import weekday

start = datetime.datetime(day=15, month=9, year=2015)
end = datetime.datetime(day=31, month=3, year=2016)

storage = 550
onetime = 26

temp = start
add = False

ans_1 = None
ans_2 = [0, 0, 0]  # [dostarczenie, palenie_d, palenie_g]
ans_3 = {}

while True:
    # morning
    print(temp.date(), storage)
    if storage < 100 and temp.weekday() == 4:
        add = True
    if not ans_1 and storage < 100:
        ans_1 = f"Rano {str(temp.date())}"
    if temp.weekday() in (5, 6) and storage > onetime:
        storage -= onetime
    else:
        pass

    # midday
    if add:
        storage += 300
        add = False
        ans_2[0] += 1

    # evening
    print(temp.date(), storage)
    if storage < 100 and not ans_1:
        ans_1 = f"Wieczór {str(temp.date())}"
    if storage > onetime:
        storage -= onetime
        ans_2[1] += 1
    else:
        ans_2[2] += 1

    ans_3[str(temp.date())] = storage

    temp += datetime.timedelta(days=1)
    if temp > end:
        break

print("#1\n", ans_1)
print("#2\n", "Dostarczono:", ans_2[0], "Palił Drewnem:", ans_2[1], "Palił Gazem:", ans_2[2])

with open('drewno.csv', 'a'):
    pass
with open('drewno.csv', 'w') as file:
    file.write("\n".join(['Dzien, ilosc dewna'] + [', '.join([k, str(v)]) for k, v in ans_3.items()]))

print("#3\n Outputed to drewno.csv, for plot refer to drewno.xlsx")
print("#4\n 468 for more refer to 2017_5_brute.py")
