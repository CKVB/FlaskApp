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

insert into users(
	guid, 
	uname, 
	upsw, 
	admin
) 
values(
	'a3a4268f-3e2c-4dda-862a-25ce8533a940',
	'king@mail.com',
	'sha256$W9WC0zo4$6b6568dc9c88b913967cc5147fab2401c7ee5a813cd08e4757031b3126dd3d1d',
	1
);