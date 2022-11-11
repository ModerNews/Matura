USE Zb111;
CREATE TABLE Zad3_temp (
    Domena text,
    IP longtext
);
INSERT INTO Zad3_temp
SELECT LEFT(m.URL ,LOCATE('/', m.URL) - 1) AS 'Domena', m.IP
FROM malware m
LEFT JOIN asn a on m.ASN = a.ASN
GROUP BY Domena, m.IP;