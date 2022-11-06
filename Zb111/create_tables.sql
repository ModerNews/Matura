-- CREATE DATABASE Zb111;
USE Zb111;
CREATE TABLE malware (
	data datetime,
	IP text,
	opis longtext,
	ASN int,
	URL longtext);
CREATE TABLE asn (
	ASN int unique,
	ID_kraju text,
	region text,
	siec longtext);
CREATE TABLE kraje (
	kraj text unique,
	ID_kraju text(2) unique);
