USE Zb111;
SELECT m.url, k.kraj, m.opis
FROM malware m 
LEFT JOIN asn a ON m.asn = a.ASN LEFT JOIN kraje k on INSTR(k.ID_kraju, a.ID_kraju) > 0
WHERE m.opis LIKE '%phish%'
