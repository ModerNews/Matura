CREATE TABLE auta (
    rejestracje text,
    marka text,
    rok int,
    pesel longtext
);
CREATE TABLE osoby (
    pesel longtext unique,
    imie longtext,
    nazwisko longtext,
    typ_miejscowosci text
);
CREATE TABLE wypadki (
    id int unique,
    data date,
    rejestracja text,
    strata float
);