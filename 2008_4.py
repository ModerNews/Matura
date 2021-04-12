slots = []
votes = []

def eval_x(votes, slots: int):
    slots = int(slots)
    x = []
    got_slots = {}
    for i in range(1, len(votes) + 1):
        got_slots[i] = 0

    for j in range(slots):
        x = []
        for i in range(len(votes)):
            x.append(votes[i] / (got_slots[i + 1] + 1))
        maxVal = max(x)
        got_slots[x.index(maxVal) + 1] += 1
        x.clear()
    # return list(got_slots.values()).index(max(got_slots.values())) + 1
    return got_slots

with open("dane.txt") as file:
    file = file.read().split("\n")[:-1]
    for line in file:
        line = line.split()
        ind = len(line) - 1
        slots.append(line[ind])
        votes.append((line[:-1]))

final = {}
for district in votes:
    for i in range(len(district)):
        district[i] = int(district[i])
        final[i + 1] = int(district[i])

print("#1\nTotal votes:")
print(final)
print("#2\nMin:")
ind = list(final.values()).index(min(final.values()))
print(final[ind + 1])
print("Max:")
ind = list(final.values()).index(max(final.values()))
print(final[ind + 1])
print("#3")
print(eval_x(votes[5], slots[5]))
print("#4")
final_slots = {}
for i in range(1, len(votes[1]) + 1):
    final_slots[i] = 0

for district in votes:
    temp = eval_x(district, slots[votes.index(district)])
    for i in range(1, len(temp) + 1):
        final_slots[i] += temp[i]

print(final_slots)
