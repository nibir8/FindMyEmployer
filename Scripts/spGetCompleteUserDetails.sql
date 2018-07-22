DROP PROCEDURE IF EXISTS spGetCompleteUserDetails;

DELIMITER $$
CREATE PROCEDURE spGetCompleteUserDetails
	(
	 myemail varchar(50)
	 )

  BEGIN
  SELECT us.userId,
  email,
  firstName,
  lastName,
  address1,
  address2,
  zipcode,
  city,
  state,
  country,
  phone,
  about ,
 current_Employer ,
 DATE_FORMAT(current_Employer_start_date, '%Y-%m-%d'),
 DATE_FORMAT(current_Employer_end_date, '%Y-%m-%d'),
 previous_Employer ,
 DATE_FORMAT(previous_Employer_start_date, '%Y-%m-%d'),
 DATE_FORMAT(previous_Employer_end_date, '%Y-%m-%d'),
 education_details_1 ,
  DATE_FORMAT(education_details_1_start_date, '%Y-%m-%d'),
   DATE_FORMAT(education_details_1_end_date, '%Y-%m-%d'),
 education_details_2 ,
  DATE_FORMAT(education_details_2_start_date, '%Y-%m-%d'),
   DATE_FORMAT(education_details_2_end_date, '%Y-%m-%d'),
 skill_1 ,
 skill_2,
 skill_3 ,
 skill_4 ,
 project_Name_1 ,
 project_Details_1 ,
 project_Name_2 ,
 project_Details_2 ,
 project_Name_3 ,
 project_Details_3,
 typeofuser,
 typeofplan
  FROM tbl_users us
  inner join  tbl_user_details ud on us.userId= ud.userId
  where email=myemail;

END$$
DELIMITER ;
