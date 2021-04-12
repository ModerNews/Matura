import pandas as pn
import logging as logger

# Grzegorz Jagielski i Michał Waluś

logger.basicConfig(filename='Korespondencja.log', level=logger.DEBUG, format='[%(levelname)s]%(message)s', filemode='w')
logger.info('Starting')

file = pn.read_excel('Baza.xlsx', usecols=[1,2,3], header=1)
tt = file.values.flatten().tolist()
dict = {}
temp1 = round(len(tt) / 3)
for i in range(temp1):
    dict[tt[i * 3]] = tt[i*3+1:(i+1)*3]
for key in dict.keys():
    f = None
    exec('open(\'' + key +'.txt\', \'w\', encoding="cp1250").close')
    exec('f = open(\'' + key +'.txt\', \'a+\', encoding="cp1250")')
    if str(dict[key][0]) == 'nan':
        logger.error('[' + key + '.txt]Provided non-numeric debt value')
    elif any(temp[-1] == 'a' for temp in key.split()):
        try:
            print(f'Szanowna Pani {key}', file=f)
            print(f'\nWzywamy Panią do natychmiastowej spłaty długu w wysokości {str(dict[key][0])} złotych.', file=f)
            print(f'Ostateczny termin spłaty to {str(dict[key][1].day)} {dict[key][1].strftime("%B")} {str(dict[key][1].year)}', file=f)
            print('Jeśli nie spłaci Pani długu w podanym terminie będziemy zmuszeni przejść na drogę sądową.', file=f)
        except (ValueError, AttributeError):
            logger.error(f'[{key}.txt]Used datetime, that doesn\'t exist ({str(dict[key][1])})')
            exec(f'open(\'{key}.txt\', \'w\').close')
    else:
        try:
            print(f'Szanowny Pan {key}', file=f)
            print(f'\nWzywamy Pana do natychmiastowej spłaty długu w wysokości {str(dict[key][0])} złotych.', file=f)
            print(f'Ostateczny termin spłaty to {str(dict[key][1].day)} {dict[key][1].strftime("%B")} {str(dict[key][1].year)}', file=f)
            print('Jeśli nie spłaci Pan długu w podanym terminie będziemy zmuszeni przejść na drogę sądową.', file=f)
        except (ValueError, AttributeError):
            logger.error(f'[{key}.txt]Used datetime, that doesn\'t exist ({str(dict[key][1])})')
            exec(f'open(\'{key}.txt\', \'w\').close')
logger.info('Finished')

