<?php
include 'config.php';
include 'error.php';


if(isset($_POST['submit_b']))
		{
			//if($_POST)
			//{
			//echo '<script type= "text/javascript"> alert("user already exists.. try another username")</script>';
			$errors = array();
			$FirstName=$LastName=$Username=$Password=$Confirmpassword=$Address=$Postal="";
			$FirstName=$_POST['FirstName'];
			$LastName=$_POST['LastName'];
			$Username=$_POST['Username'];
			$Password=$_POST['Password'];
			$Confirmpassword=$_POST['Confirmpassword'];
			$Address=$_POST['Address'];
			$Postal=$_POST['Postal'];
			
			if (empty($FirstName)) { array_push($errors, "First name is required"); }
			if(!preg_match("/^[a-zA-Z]+$/",$FirstName)) { array_push($errors, "First name is invalid"); }
			if (empty($LastName)) { array_push($errors, "Last name is required"); }
			if(!preg_match("/^[a-zA-Z ,.'-]+$/",$LastName)) { array_push($errors, "Last name is invalid"); }
			if (empty($Username)) { array_push($errors, "Email ID/Username is required"); }
			if(!filter_var($Username, FILTER_VALIDATE_EMAIL)) { array_push($errors, "Email ID is invalid"); }
			if (empty($Password)) { array_push($errors, "Password is required"); }
			if(strlen($Password) < 8){ array_push($errors, "Password length should be minimum of 8 characters"); }
			if (empty($Confirmpassword)) { array_push($errors, "Confirm password is required"); }
			if(!preg_match("/^\s*\S+(?:\s+\S+){2}/",$Address)) { array_push($errors, "Invalid address"); }
			if(!preg_match("/^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$/",$Postal)) { array_push($errors, "Invalid postal"); }
			if ($Password != $Confirmpassword) {array_push($errors, "The passwords do not match"); }
			
			
			
			
			
				if(count($errors) == 0)
				{
				$Password = md5($password_1);
				$query=$con->prepare("select * from login WHERE username ='$Username'");
				$query->execute();
				$row_count=$query->rowCount();
				
				if($row_count>0)
				{
					array_push($errors, "user exits"); 
					
				}
				else 
				{
				$sql="insert into login values('$Username','$Password','$FirstName','$LastName','$Address','$Postal')";
				$con->exec($sql);
				$query_run=mysqli_query($con,$query);
					echo "New record created successfully";
					header('location: login.php');	
				}
				}
				
		}	
		
	
		
?>