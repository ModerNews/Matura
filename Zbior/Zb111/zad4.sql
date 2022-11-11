USE Zb111;
SELECT MONTH(malware.data) AS 'Miesiąc', a.region, COUNT(malware.data) AS "Malware'y"
FROM malware
INNER JOIN asn a on malware.ASN = a.ASN
WHERE (a.region = 'apnic' OR a.region = 'arin' OR a.region = 'lacnic' OR a.region = 'ripencc' OR a.region = 'afrinic')
AND YEAR(malware.data) = 2014
GROUP BY Miesiąc, a.region