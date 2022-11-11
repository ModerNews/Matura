import sqlite3

mydb = sqlite3.connect("2011_5.db")
cur = mydb.cursor()

with open("2011_res\\osoby.txt", "r") as file:
    data = file.read().split("\n")[:-1]

cur.execute('CREATE TABLE "osoby" ("id_osoby" TEXT,"imie" TEXT,"nazwisko" TEXT,"tel" TEXT)')

for line in data:
    line = line.split(";")
    cur.execute("INSERT INTO osoby VALUES ('{}', '{}', '{}', '{}')".format(line[0], line[1], line[2], line[3]))

mydb.commit()

cur.execute('CREATE TABLE "psy" ("id_psa" INTEGER, "rasa" TEXT, "wiek" INTEGER, "plec" TEXT, "medale" INTEGER, "id_osoby" TEXT)')
with open("2011_res\\psy.txt", "r") as file:
    data = file.read().split("\n")[:-1]

for line in data:
    line = line.split(";")
    cur.execute("INSERT INTO psy VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(line[0], line[1], line[2], line[3], line[4], line[5]))

mydb.commit()
print(cur.execute("SELECT * FROM osoby").fetchall())