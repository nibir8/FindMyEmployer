
DROP PROCEDURE spCreateUser

DELIMITER $$
CREATE PROCEDURE spCreateUser
(
 mypassword varchar(50),
 myemail varchar(50),
 myfirstname varchar(50),
 mylastname varchar(50),
 myaddress1 varchar(50),
myaddress2 varchar(50),
 myzipcode varchar(50),
 mycity varchar(50),
 mystate varchar(50),
 mycountry varchar(50),
 myphone varchar(50),
myusertype varchar(50),
myplantype varchar(50)
 )
 BEGIN

 DECLARE myuserid INTEGER;

INSERT INTO tbl_users (password, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone,typeofuser,typeofplan)
VALUES (mypassword, myemail, myfirstname , mylastname, myaddress1,myaddress2 ,myzipcode ,mycity ,mystate,mycountry,myphone,myusertype,myplantype);



Select @myuserid := userid  From tbl_users where email = myemail;

INSERT
into
tbl_user_details
(
userId,
email_id,
about ,
current_Employer ,
current_Employer_start_date ,
current_Employer_end_date ,
previous_Employer ,
previous_Employer_start_date ,
previous_Employer_end_date ,
education_details_1 ,
education_details_1_start_date ,
education_details_1_end_date ,
education_details_2 ,
education_details_2_start_date ,
education_details_2_end_date ,
skill_1 ,
skill_2,
skill_3 ,
skill_4 ,
project_Name_1 ,
project_Details_1 ,
project_Name_2 ,
project_Details_2 ,
project_Name_3 ,
project_Details_3
) values
 (
 @myuserid ,
 myemail,
 '',
  '',
 '1900-01-01',
 '1900-01-01',
   '',
 '1900-01-01',
 '1900-01-01',
  '',
 '1900-01-01',
 '1900-01-01',
 '',
 '1900-01-01',
 '1900-01-01',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '',
 '');

END$$
DELIMITER ;
