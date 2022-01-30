import sqlite3

mydb = sqlite3.connect("2011_5.db")
cur = mydb.cursor()

with open("2011_res\\osoby.txt", "r") as file:
    data = file.read().split("\n")[:-1]

for line in data:
    line = line.split(";")
    cur.execute("INSERT INTO osoby VALUES ('{}', '{}', '{}', '{}')".format(line[0], line[1], line[2], line[3]))

mydb.commit()

with open("2011_res\\psy.txt", "r") as file:
    data = file.read().split("\n")[:-1]

for line in data:
    line = line.split(";")
    cur.execute("INSERT INTO psy VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(line[0], line[1], line[2], line[3], line[4], line[5]))

mydb.commit()
print(cur.execute("SELECT * FROM osoby").fetchall())