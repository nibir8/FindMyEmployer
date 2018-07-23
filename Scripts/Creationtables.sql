
DROP TABLE IF EXISTS tbl_users;
DROP TABLE IF EXISTS tbl_jobs;
DROP TABLE IF EXISTS tbl_user_status;
DROP TABLE IF EXISTS tbl_user_details;


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
phone varchar(50),
typeofuser varchar(50),
typeofplan varchar(50)
);


CREATE TABLE tbl_Jobs
(
postingId INTEGER PRIMARY KEY AUTO_INCREMENT,
jobId INTEGER,
companyName varchar(50),
title varchar(50),
manager varchar(50),
location varchar(50),
jobDetails varchar(50),
emailid varchar(50)
);


CREATE TABLE tbl_user_status
(
status_id  INTEGER PRIMARY KEY AUTO_INCREMENT,
email varchar(50),
userstatus varchar(500),
userId integer,
firstname varchar(50),
lastname varchar(50),
FOREIGN KEY (userId) REFERENCES tbl_users(userId)
);

Create table tbl_user_details
(
userDetailId INTEGER PRIMARY KEY AUTO_INCREMENT,
userId INTEGER,
email_id varchar(50),
about varchar(500),
 current_Employer varchar(500),
 current_Employer_start_date date,
 current_Employer_end_date date,
 previous_Employer varchar(500),
 previous_Employer_start_date date,
 previous_Employer_end_date date,
 education_details_1 varchar(50),
 education_details_1_start_date date,
 education_details_1_end_date date,
 education_details_2 varchar(500),
 education_details_2_start_date date,
 education_details_2_end_date date,
 skill_1 varchar(50),
 skill_2 varchar(50),
 skill_3 varchar(50),
 skill_4 varchar(50),
 project_Name_1 varchar(50),
 project_Details_1 varchar(500),
 project_Name_2 varchar(50),
 project_Details_2 varchar(500),
 project_Name_3 varchar(50),
 project_Details_3 varchar(500),
FOREIGN KEY (userId) REFERENCES tbl_users(userId)
);

CREATE TABLE tbl_JobsApplication
(
application_id  INTEGER PRIMARY KEY AUTO_INCREMENT,
email varchar(50)
);
