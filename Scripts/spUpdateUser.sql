
drop procedure spUpdateUser;

DELIMITER $$
CREATE PROCEDURE spUpdateUser
(
 myemail varchar(50),
 myfirstname varchar(50),
 mylastname varchar(50),
 myaddress1 varchar(50),
 myaddress2 varchar(50),
 mycity varchar(50),
myzipcode varchar(50),
 mystate varchar(50),
 mycountry varchar(50),
 myphone varchar(50),
 myabout varchar(500),
 myCurrent_Employer varchar(500),
 myCurrent_Employer_start_date date,
 myCurrent_Employer_end_date date,
 myPrevious_Employer varchar(500),
 myPrevious_Employer_start_date date,
 myPrevious_Employer_end_date date,
 myEducation_details_1 varchar(50),
 myEducation_details_1_start_date date,
 myEducation_details_1_end_date date,
 myEducation_details_2 varchar(500),
 myEducation_details_2_start_date date,
 myEducation_details_2_end_date date,
 mySkill_1 varchar(50),
 mySkill_2 varchar(50),
 mySkill_3 varchar(50),
 mySkill_4 varchar(50),
 myProject_Name_1 varchar(50),
 myProject_Details_1 varchar(500),
 myProject_Name_2 varchar(50),
 myProject_Details_2 varchar(500),
 myProject_Name_3 varchar(50),
 myProject_Details_3 varchar(500)
 )
 BEGIN

DECLARE myuserid INTEGER;

Select @myuserid := userid  From tbl_users where email = myemail;

 update tbl_users
 set firstname = myfirstname,
 lastname = mylastname,
 address1 = myaddress1,
 address2 = myaddress2,
 zipcode = myzipcode,
 city = mycity,
 state = mystate,
 country = mycountry,
 phone = myphone
 where  email = myemail;

  update tbl_user_details
  SET
  about = myabout,
  current_Employer = myCurrent_Employer ,
 current_Employer_start_date = myCurrent_Employer_start_date ,
 current_Employer_end_date = myCurrent_Employer_end_date ,
 previous_Employer = myPrevious_Employer ,
 previous_Employer_start_date= myPrevious_Employer_start_date ,
 previous_Employer_end_date = myPrevious_Employer_end_date ,
 education_details_1 = myEducation_details_1 ,
 education_details_1_start_date= myEducation_details_1_start_date ,
 education_details_1_end_date= myEducation_details_1_end_date ,
 education_details_2 = myEducation_details_2 ,
 education_details_2_start_date = myEducation_details_2_start_date ,
 education_details_2_end_date = myEducation_details_2_end_date ,
 skill_1= mySkill_1 ,
 skill_2 = mySkill_2 ,
 skill_3 = mySkill_3 ,
 skill_4 = mySkill_4 ,
 project_Name_1 = myProject_Name_1 ,
 project_Details_1 = myProject_Details_1 ,
 project_Name_2 = myProject_Name_2 ,
 project_Details_2 = myProject_Details_2 ,
 project_Name_3 = myProject_Name_3 ,
 project_Details_3 = myProject_Details_3
 where userid = @myuserid ;


END$$
DELIMITER ;
