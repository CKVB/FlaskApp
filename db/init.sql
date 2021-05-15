CREATE DATABASE usersDataBase;
use usersDataBase;

CREATE TABLE users(
	uid integer auto_increment,
	guid varchar(180) not null,
	uname varchar(45) not null,
	upsw varchar(180),
	admin boolean,
	primary key(uid),
	unique (guid), 
	unique(uname)
);