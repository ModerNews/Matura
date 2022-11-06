SELECT k.kraj, RIGHT(malware.URL, 4) AS 'filetype', COUNT(malware.IP) AS 'entries'
FROM malware LEFT JOIN asn a ON malware.ASN = a.ASN LEFT JOIN kraje k on INSTR(k.ID_kraju, a.ID_kraju) > 0
WHERE RIGHT(malware.URL, 4) LIKE '%png%' OR RIGHT(malware.URL, 4) LIKE '%jpg%'
GROUP BY filetype, a.ID_kraju;
