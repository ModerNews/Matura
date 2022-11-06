USE Zb111;
SELECT k.kraj, a.siec, COUNT(m.url) as 'Domeny', COUNT(DISTINCT m.IP) as 'IP'
FROM asn a
LEFT JOIN malware m on a.ASN = m.ASN LEFT JOIN kraje k ON INSTR(k.ID_kraju, a.ID_kraju) > 0
GROUP BY a.ASN
ORDER BY Domeny DESC
LIMIT 5;