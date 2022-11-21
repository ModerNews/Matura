USE 2008_6;
SELECT SUM(plw.liczba_wypadkow)
FROM (SELECT auta.pesel, COUNT(DISTINCT wypadki.id) AS 'liczba_wypadkow'
FROM wypadki LEFT JOIN auta ON wypadki.rejestracja = auta.rejestracje
GROUP BY auta.pesel
HAVING COUNT(DISTINCT wypadki.id) >= 1) as plw;