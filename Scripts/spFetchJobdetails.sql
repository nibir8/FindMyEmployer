DROP PROCEDURE IF EXISTS spFetchJobdetails

CREATE PROCEDURE  spFetchJobdetails
()
Select *From tbl_Jobs
