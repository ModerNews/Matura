USE Zb111;
SELECT Domena, COUNT(DISTINCT IP) AS 'Liczba_IP'
FROM Zad3_temp
GROUP BY Domena
HAVING Liczba_IP >= 2
ORDER BY Liczba_IP DESC;