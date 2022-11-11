import datetime

start = datetime.datetime(2011, 4, 1)
temp = start
end = start + datetime.timedelta(days=100)
grass = 10000
cars = 30
change = 0.97
temp_grass = 0

for grass in (10000, 7000, 4000):
    temp = start
    while True:
        # print(temp, grass)
        # 2.2
        # if temp_grass == grass:
        #     print((start - temp).days)
        #     break
        # 2.3
        # if temp == datetime.datetime(2011, 4, 12):
        #     while True:
        #         temp_grass = grass - cars * 15
        #         if temp_grass <= 0:
        #             print(cars)
        #             break
        #         else:
        #             cars += 1
        #     break
        grass -= cars * 15
        grass += 600
        grass = int(grass * change)
        # print("\n")
        temp = temp + datetime.timedelta(days=1)
        if temp >= end: break
    print(grass)


print("#1 - 271")
print("#2 1 Fałsz\n2 Prawda Po 185 dniach [...] jest to 03-10-2011 3 Prawda 569 samochodów")
print("#3 5079, 4937, 4792")