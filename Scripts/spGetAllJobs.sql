DROP PROCEDURE spGetAllJobs;
CREATE PROCEDURE spGetAllJobs
  (
  myEmail varchar(50)
  )

  Select * From tbl_Jobs where emailid = myEmail;
