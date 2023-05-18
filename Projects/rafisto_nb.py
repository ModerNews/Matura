import math
import numpy as np

from matplotlib import pyplot as plt

start_year = 2019

data = [167, 184, 242]
diffs = [data[i] - data[i - 1] for i in range(1, len(data))]
diff_change = [diffs[i - 1] / diffs[i] for i in range(1, len(diffs))]
diff_change = sum(diff_change) / len(diff_change)
print(diff_change)

while data[-1] < 186*28:
    diff = diffs[-1] * (1 + diff_change)
    diffs.append(diff)
    data.append(data[-1] + diff)

z = np.polyfit(list(range(len(data))), data, 3)
p = np.poly1d(z)

print(p(list(range(len(data)))))

ax = plt.axes()
ax.set_facecolor('xkcd:light grey')

plt.plot([f"{start_year + i}/{start_year + i + 1}" for i in range(len(data))], data, figure=plt.figure(figsize=(19, 10)), color='blue')
plt.plot([f"{start_year + i}/{start_year + i + 1}" for i in range(len(data))], p(list(range(len(data)))), color='red', linestyle='--')
plt.yticks([150 + i * 250 for i in range(0, math.floor(data[-1] / 250))])
plt.grid(True)
plt.scatter([f"{start_year + i}/{start_year + i + 1}" for i in range(len(data))], data, color='orange')
for value in data:
    plt.annotate(round(value, 0), (data.index(value), value), va='bottom', ha='right')
plt.ylabel('Godziny nieobecności')
plt.xlabel('Rok szkolny')
plt.title('Przewidywana liczba godzin nieobecności Rafist0 w następnych latach')
plt.annotate(f'Ilość godzin w roku szkolnym: {186*28}', (0, 186*28))
plt.plot(list(range(len(data))), [186*28 for i in range(len(data))], color='orange', linestyle='--')
# plt.plot(list(range(len(data))), [365*28 + 365*28*0.1 for i in range(len(data))], color='purple', linestyle='--')
# plt.plot(data[idx], 186*28, 'ro')
plt.show()