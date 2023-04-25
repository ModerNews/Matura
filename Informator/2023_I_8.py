import datetime

with open('DANE/zamowienia.csv', 'r') as file:
    data = [[datetime.datetime.strptime(params[0], '%d/%m/%Y').date(), int(params[1])] for line in file.read().split('\n')[1:-1] if (params := line.split('\t'))]

output = ''

for y in range (2018, 2020):
    for m in range(1, 13):
        output += f'{y} {m}; {sum([x[1] for x in data if x[0].month == m and x[0].year == y])}\n'

with open('2023_I_8.csv', 'w') as file:
    file.write(output)

capacity = 400
requests_sum = 0
transport_days = 0

start_date = data[0][0]
end_date = data[-1][0]
current_date = start_date

output_3 = []

base = 200
state = 1000

multiplier = 1.0
last_multiplier = 1.0
count, max_count = 0, 0
multiplier_chain_start_date, max_multiplier_chain_start_date = start_date, start_date

i = 0
while current_date < end_date:
    if current_date == data[i][0]:
        requests_sum += data[i][1]
        i += 1

    if state > 1500:
        multiplier = 0.8
    elif requests_sum > state/2:
        multiplier = 1.3
    else:
        multiplier = 1.0

    print(f'{current_date} {requests_sum} {state} {multiplier}')
    if multiplier == last_multiplier:
        count += 1
    else:
        if count > max_count:
            max_count = count
            max_multiplier_chain_start_date = multiplier_chain_start_date
        count = 0
        last_multiplier = multiplier
        multiplier_chain_start_date = current_date

    state += multiplier * base

    if requests_sum >= capacity:
        if (requests_sum // capacity) >= 2:
            output_3.append(current_date)

        transport_days += 1
        state -= capacity * (requests_sum // capacity)
        requests_sum -= capacity * (requests_sum // capacity)

    current_date += datetime.timedelta(days=1)

print('10.2 ' + str(transport_days))
print('10.3\n' + '\n'.join([str(date) for date in output_3]))
print('10.4 ' + str(max_count) + ' ' + str(multiplier_chain_start_date))