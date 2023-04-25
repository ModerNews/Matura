import datetime

with open('res/soki.txt', 'r+') as file:
    # data, magazyn, wielkosc
    data = {line[0]: line[1:] for tmp in file.read().split('\n')[1:-1] if (line := tmp.split('\t'))}

mag = 30000
# start_data = datetime.date()
current_date = datetime.datetime(2021, 1, 2)
i = 1
stopper = False
total_handled_by_side = []
first_handle = [None, 0]
magazines = {}

while not stopper:
    if current_date.weekday() not in (5, 6):
        mag += 12000
    else:
        mag += 5000

    while not stopper:
        if i > len(data):
            stopper = True
            break
        if (test_date := datetime.datetime.strptime(data[str(i)][0], "%d.%m.%Y")).date() == current_date.date():
            print(f'{current_date.strftime("%d.%m.%Y")} {i} {data[str(i)][1]}')
            try:
                magazines[data[str(i)][1]] += 1
            except KeyError:
                magazines[data[str(i)][1]] = 1

            if mag < int(data[str(i)][2]):
                print(f'Handled by side company: {current_date.strftime("%d.%m.%Y")} {i} {data[str(i)][2]}')
                total_handled_by_side += [int(data[str(i)][2])]
                if not first_handle[0]:
                    first_handle = [current_date, i]
            else:
                mag -= int(data[str(i)][2])
            i += 1
        else:
            break

    # print(f'{current_date} {mag} {i}')
    current_date += datetime.timedelta(days=1)

tmp = '\n'.join([f"{key}: {value}" for key, value in magazines.items()])
print(f"5.1\n{tmp}")
print(f'#5.4\nData: {first_handle[0].strftime("%d.%m.%Y")}\nID: {first_handle[1]}\nLiczba zamówień: {len(total_handled_by_side)}\nSuma: {sum(total_handled_by_side)}')