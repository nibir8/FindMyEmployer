DROP PROCEDURE spGetUserApplications;
CREATE PROCEDURE spGetUserApplications
  (
  myEmail varchar(50)
  )
  Select * From tbl_JobsApplication where email = myEmail
