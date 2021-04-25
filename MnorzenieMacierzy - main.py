import Matrix
import numpy as np
import time
import traceback
import os

print('Program przemnoży przez siebie dowolną ilość macierzy\n(Najpierw czystym pythonem, następnie z użyciem bibliotek Numpy i wskaże czasy wykonywania)'
      '\nDane wejściowe należy umieścić w pliku Matrix.txt,'
      '\noddzielając kolejne macierze poejdynczymi linijkami przerwy\n(tak jak pokazują to przykładowe macierze już umieszczone w pliku).'
      '\nPo zakończeniu kliknij Enter...')
input()

with open('Matrix.txt') as file:
    lines = file.read().split("\n")

matrices = []
n = lines.count('')
i = 0
for line in lines:
    if line == '':
        i += 1
        if i > n:
            break
    else:
        line = line.split()
        for x in line:
            line[line.index(x)] = int(x)
        try:
            matrices[i].append(line)
        except IndexError:
            matrices.append([])
            matrices[i].append(line)

print('Clear python solution:')
start_time = time.time()
C = matrices[0]
try:
    for i in range(1, len(matrices)):
        try:
            C = Matrix.dot(C, matrices[i])
        except IndexError:
            traceback.print_exc()
            pass
    if len(C) == 2:
        C = C[1]
    for line in C:
        print(line)
except ValueError:
    print('Unable to multiply those matrices into')

print(f'took {time.time() - start_time}')

print('Numpy solution:')
start_time2 = time.time()
C = np.matrix(matrices[0], dtype='int64')
for i in range(1, len(matrices)):
    try:
        B = np.matrix(matrices[i], dtype='int64')
        C = C.dot(B)
    except IndexError:
        traceback.print_exc()
        pass
    except ValueError:
        print('Unable to multiply those matrices')
        break
print(C)
print(f'took {time.time() - start_time2}')
