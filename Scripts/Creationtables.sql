
DROP TABLE IF EXISTS tbl_users;
DROP TABLE IF EXISTS tbl_jobs;

CREATE TABLE tbl_users
(
userId INTEGER PRIMARY KEY AUTO_INCREMENT,
password varchar(50),
email varchar(50),
firstName varchar(50),
lastName varchar(50),
address1 varchar(50),
address2 varchar(50),
zipcode varchar(50),
city varchar(50),
state varchar(50),
country varchar(50),
phone varchar(50)
)


CREATE TABLE tbl_Jobs
(
jobId INTEGER PRIMARY KEY,
companyName varchar(50),
title varchar(50),
manager varchar(50),
location varchar(50),
jobDetails varchar(50)
)
