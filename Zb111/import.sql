USE Zb111;
LOAD DATA LOCAL INFILE '/home/gruzin/PycharmProjects/Matura/Zb111/asn.txt' INTO TABLE asn FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE '/home/gruzin/PycharmProjects/Matura/Zb111/kraje.txt' INTO TABLE kraje FIELDS TERMINATED BY '\t';
LOAD DATA LOCAL INFILE '/home/gruzin/PycharmProjects/Matura/Zb111/malware.txt' INTO TABLE malware FIELDS TERMINATED BY '\t';

DELETE FROM kraje WHERE kraj LIKE 'kraj'