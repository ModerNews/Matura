import sqlite3

mydb = sqlite3.connect("2011_5.db")
cur = mydb.cursor()

print("#1", cur.execute("SELECT plec, COUNT(plec) FROM psy GROUP BY plec").fetchall())

print("#2", cur.execute('SELECT osoby.imie, osoby.nazwisko, COUNT(psy.id_psa) AS ilosc FROM psy LEFT JOIN osoby ON psy.id_osoby=osoby.id_osoby GROUP BY osoby.id_osoby HAVING ilosc > 8 ORDER BY osoby.nazwisko').fetchall())

print("#3", cur.execute('SELECT osoby.imie, osoby.nazwisko, SUM(psy.medale) AS medale FROM psy LEFT JOIN osoby ON psy.id_osoby=osoby.id_osoby GROUP BY osoby.id_osoby ORDER BY medale DESC LIMIT 1').fetchone())

print("#4", sum([row[0] for row in cur.execute('SELECT COUNT(osoby.id_osoby) AS liczba FROM psy LEFT JOIN osoby ON psy.id_osoby=osoby.id_osoby GROUP BY rasa HAVING psy.rasa LIKE "%owczarek%"').fetchall()]))