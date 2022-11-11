import logging as logger

logger.basicConfig(filename='Ciagi.log', level=logger.DEBUG, format='[%(levelname)s] %(message)s', filemode='w')
logger.info('Starting')

with open('../dane4.txt', 'r') as file:
    series = file.read().split()

differs = []
for num in series:
    try:
        differs.append(abs(int(num) - int(series[series.index(num) + 1])))
    except IndexError:
        logger.info('End of Series')

print('# 4.1')
print('Największa: ' + str(max(differs)))
print('Najmniejsza: ' + str(min(differs)))

print('# 4.2')
serie_len = 0
start_index = 0
end_index = 0
for i in range(serie_len, len(differs)):
    tempLen = 1
    for j in range(i, len(differs)):
        if differs[i] == differs[j]:
            tempLen += 1
        else:
            break
    if tempLen > serie_len:
        serie_len = tempLen
        start_index = i
        end_index = j

print('Największa długość fragmentu regularnego: ' + str(serie_len))
print('Początek: ' + str(series[start_index]))
print('Koniec: ' + str(series[end_index]))

print('# 4.3')
counter = {}
for num in differs:
    if num not in counter.keys():
        counter[num] = 1
    else:
        counter[num] += 1

max_value = max(list(counter.values()))
values = [k for k, v in counter.items() if v == max_value]
print(f'Wartości najczęstszych luk: {values}')
print(f'Krotność najczęstszej luki: {counter[values[0]]}')
