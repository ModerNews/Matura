USE 2008_6;
LOAD DATA LOCAL INFILE '/home/gruzin/PycharmProjects/Matura_new/2008/auta.txt' INTO TABLE auta FIELDS TERMINATED BY ' ';
LOAD DATA LOCAL INFILE '/home/gruzin/PycharmProjects/Matura_new/2008/osoby.txt' INTO TABLE osoby FIELDS TERMINATED BY ' ';
LOAD DATA LOCAL INFILE '/home/gruzin/PycharmProjects/Matura_new/2008/wypadki.txt' INTO TABLE wypadki FIELDS TERMINATED BY ' ';