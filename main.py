from module_settings import *

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static' + '/images'
mysql.init_app(app)
app.secret_key = 'random string'
mail = Mail(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image Only!'), FileRequired(u'Choose a file!')])
    submit = SubmitField(u'Upload')

@app.route("/")
def root():
    try:
        if 'email' not in session:
            loggedIn = False
            firstName = ''
            return render_template('home.html',  loggedIn=loggedIn, firstName=firstName)
        else:
            StatusData = []
            captureSessionid.emailid =  session['email']
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            loginclassdetails = LoginMyClass.LoginMyClass(session['email'],'','','','','')
            loggedIn, firstName, typeOfUser = loginclassdetails.getMyLoginDetails()
            fetchuserstatus = FetchAllUserStatuses.FetchAllUserStatuses(StatusData,'')
            StatusData,message = fetchuserstatus.getAllUserStatus()
            return render_template("Profile2.html",loggedIn=loggedIn, firstName=firstName,userStatus=StatusData,profileData=profileData)
    except Exception as e:
        excep_msg = "Error in view Homepage"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/account/profile")
def profileHome():
    try:
        if 'email' not in session:
            return redirect(url_for('root'))
        else:
            loggedIn = True
            StatusData = []
            loginclassdetails = LoginMyClass.LoginMyClass(session['email'],'','','','','')
            loggedIn, firstName, typeOfUser = loginclassdetails.getMyLoginDetails()
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            fetchuserstatus = FetchAllUserStatuses.FetchAllUserStatuses(StatusData,'')
            StatusData,message = fetchuserstatus.getAllUserStatus()
            return render_template("Profile2.html",loggedIn=loggedIn, firstName=firstName,userStatus=StatusData,profileData=profileData)
    except Exception as e:
        excep_msg = "Error in view profile"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/account/profile/edit")
def editProfile():
    try:
        if 'email' not in session:
            return redirect(url_for('root'))
        loginclassdetails = LoginMyClass.LoginMyClass(session['email'],'','','','','')
        loggedIn, firstName, typeOfUser = loginclassdetails.getMyLoginDetails()

        fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
        profileData,msg = fetchuserdata.getMyProfileData()
        return render_template("editProfile.html", profileData=profileData, loggedIn=loggedIn, firstName=firstName )
    except Exception as e:
        excep_msg = "Error in view edit profile"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/account/profile/changePassword", methods=["GET", "POST"])
def changePassword():
    try:
        if 'email' not in session:
            return redirect(url_for('loginForm'))
        if request.method == "POST":
            oldPassword = request.form['oldpassword']
            newPassword = request.form['newpassword']
            hashmychangingpassword = HashMyChangingPassword.HashMyChangingPassword(session['email'],oldPassword,newPassword,'')
            msg = hashmychangingpassword.hashMyChangingPassword()
            return render_template("changePassword.html", msg=msg)
        else:
            return render_template("changePassword.html")
    except Exception as e:
        excep_msg = "Error in view changepassword"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/updateProfile", methods=["GET", "POST"])
def updateProfile():
    try:
        if request.method == 'POST':
            email = request.form['email']
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            address1 = request.form['address1']
            address2 = request.form['address2']
            zipcode = request.form['zipcode']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            phone = request.form['phone']
            user_details = []
            About = request.form['About']
            Current_Employer = request.form['Current_Employer']
            Current_Employer_start_date = request.form['Current_Employer_start_date']
            Current_Employer_end_date = request.form['Current_Employer_end_date']
            Previous_Employer = request.form['Previous_Employer']
            Previous_Employer_start_date = request.form['Previous_Employer_start_date']
            Previous_Employer_end_date = request.form['Previous_Employer_end_date']
            Education_details_1 = request.form['Education_details_1']
            Education_details_1_start_date = request.form['Education_details_1_start_date']
            Education_details_1_end_date = request.form['Education_details_1_end_date']
            Education_details_2 = request.form['Education_details_2']
            Education_details_2_start_date = request.form['Education_details_2_start_date']
            Education_details_2_end_date = request.form['Education_details_2_end_date']
            Skill_1 = request.form['Skill_1']
            Skill_2 = request.form['Skill_2']
            Skill_3 = request.form['Skill_3']
            Skill_4 = request.form['Skill_4']
            Project_Name_1 = request.form['Project_Name_1']
            Project_Details_1 = request.form['Project_Details_1']
            Project_Name_2 = request.form['Project_Name_2']
            Project_Details_2 = request.form['Project_Details_2']
            Project_Name_3 = request.form['Project_Name_3']
            Project_Details_3 = request.form['Project_Details_3']
            user_details.append(About)
            user_details.append(Current_Employer)
            user_details.append(Current_Employer_start_date)
            user_details.append(Current_Employer_end_date)
            user_details.append(Previous_Employer)
            user_details.append(Previous_Employer_start_date)
            user_details.append(Previous_Employer_end_date)
            user_details.append(Education_details_1)
            user_details.append(Education_details_1_start_date)
            user_details.append(Education_details_1_end_date)
            user_details.append(Education_details_2)
            user_details.append(Education_details_2_start_date)
            user_details.append(Education_details_2_end_date)
            user_details.append(Skill_1)
            user_details.append(Skill_2)
            user_details.append(Skill_3)
            user_details.append(Skill_4)
            user_details.append(Project_Name_1)
            user_details.append(Project_Details_1)
            user_details.append(Project_Name_2)
            user_details.append(Project_Details_2)
            user_details.append(Project_Name_3)
            user_details.append(Project_Details_3)
            updatemyprofile = UpdateMyGivenProfile.UpdateMyGivenProfile(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details,myUser.userType,myUser.planType,'')
            msg = updatemyprofile.updateMyProfileMethod()
            return redirect(url_for('editProfile',msg=msg))
    except Exception as e:
        excep_msg = "Error in view update profile"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/postStatus" , methods=['POST'])
def postStatus():
    try:
        text = request.form['inputPost']
        insertuserstatus = PostUserStatus.PostUserStatus(session['email'],text,'')
        message = insertuserstatus.insertUserStatus()
        return redirect(url_for('profileHome'))
    except Exception as e:
        excep_msg = "Error in view poststatus"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/loginForm")
def loginForm():
    try:
        if 'email' in session:
            return redirect(url_for('root'))
        else:
            return render_template('home.html', error='')
    except Exception as e:
        excep_msg = "Error in view loginform"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/login", methods = ['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            value = ""
            factoryObject = FactoryPattern.FactoryPattern()
            factoryObject_Validator_emailNullCheck = factoryObject.factoryPattern('Email NullCheck')
            checkEmailNull = factoryObject_Validator_emailNullCheck.formValidate_BSL(email)
            factoryObject_Validator_passNullCheck = factoryObject.factoryPattern('Password NullCheck')
            checkPassNull = factoryObject_Validator_passNullCheck.formValidate_BSL(password)
            if ((not checkEmailNull)and(not checkPassNull)):
                checkifuservalid = CheckIfMyUserValid.CheckIfMyUserValid(email,password,'','')
                value = checkifuservalid.isValid()
                checkEmailNull = ""
                checkPassNull = ""
                if (value == True):
                    session['email'] = email
                    return redirect(url_for('root'))
                else:
                    return render_template('home.html', passwordNull=checkPassNull,userPassIncorrect=value)
            else:
	            return render_template('home.html', passwordNull=checkPassNull,userPassIncorrect=value)
    except Exception as e:
        excep_msg = "Error in view login"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/logout")
def logout():
    try:
        session.pop('email', None)
        return redirect(url_for('root'))
    except Exception as e:
        excep_msg = "Error in view logout"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            #Parse form data
            password = request.form['password']
            cpassword = request.form['cpassword']
            email = request.form['email']
            email = email.lower()
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            address1 = request.form['address1']
            address2 = request.form['address2']
            zipcode = request.form['zipcode']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            phone = request.form['phone']
            userType = request.form['userOptions']
            planType = request.form['planOptions']
            reader = XmlReader.XmlReader()
            EmployeePlanName,EmployeePlanCount,EmployeePlanPrice,EmployeeMessagePermission = reader.readmyFile("employee")
            noOfPlansEmployee = len(EmployeePlanName)
            EmployerPlanName,EmployerPlanCount,EmployerPlanPrice,EmployerMessagePermission = reader.readmyFile("employer")
            noOfPlansEmployer = len(EmployerPlanName)
            user_details = []
            factoryObject = FactoryPattern.FactoryPattern()
            factoryObject_Validator_firstNameSpaceCheck = factoryObject.factoryPattern('FirstName SpaceCheck')
            checkfirstNameSpaceCheck = factoryObject_Validator_firstNameSpaceCheck.formValidate_BSL(firstName)
            if (checkfirstNameSpaceCheck != firstName):
                return render_template("register.html", error=checkfirstNameSpaceCheck,EmployeePlanName=EmployeePlanName,EmployeePlanCount=EmployeePlanCount,EmployeePlanPrice=EmployeePlanPrice,EmployeeMessagePermission=EmployeeMessagePermission,noOfPlansEmployee=noOfPlansEmployee,
                EmployerPlanName=EmployerPlanName,EmployerPlanCount=EmployerPlanCount,EmployerPlanPrice=EmployerPlanPrice,EmployerMessagePermission=EmployerMessagePermission,noOfPlansEmployer=noOfPlansEmployer)
            factoryObject_Validator_passwordSpaceCheck = factoryObject.factoryPattern('Password SpaceCheck')
            checkPasswordSpaceCheck = factoryObject_Validator_passwordSpaceCheck.formValidate_BSL(password)
            if (checkPasswordSpaceCheck != password):
                return render_template("register.html", error=checkPasswordSpaceCheck,EmployeePlanName=EmployeePlanName,EmployeePlanCount=EmployeePlanCount,EmployeePlanPrice=EmployeePlanPrice,EmployeeMessagePermission=EmployeeMessagePermission,noOfPlansEmployee=noOfPlansEmployee,
                EmployerPlanName=EmployerPlanName,EmployerPlanCount=EmployerPlanCount,EmployerPlanPrice=EmployerPlanPrice,EmployerMessagePermission=EmployerMessagePermission,noOfPlansEmployer=noOfPlansEmployer)
            factoryObject_Validator_passwordEquateCheck = factoryObject.factoryPattern('Password Equate')
            checkPasswordEquate = factoryObject_Validator_passwordEquateCheck.formValidate_BSL(password,cpassword)
            if (checkPasswordEquate != password):
                return render_template("register.html", error=checkPasswordEquate,EmployeePlanName=EmployeePlanName,EmployeePlanCount=EmployeePlanCount,EmployeePlanPrice=EmployeePlanPrice,EmployeeMessagePermission=EmployeeMessagePermission,noOfPlansEmployee=noOfPlansEmployee,
                EmployerPlanName=EmployerPlanName,EmployerPlanCount=EmployerPlanCount,EmployerPlanPrice=EmployerPlanPrice,EmployerMessagePermission=EmployerMessagePermission,noOfPlansEmployer=noOfPlansEmployer)
            factoryObject_Validator_emailValidateCheck = factoryObject.factoryPattern('Email Validate')
            checkEmailValidate = factoryObject_Validator_emailValidateCheck.formValidate_BSL(email)
            if (checkEmailValidate == email):
                fetchuserdata = FetchMyUserData.FetchMyUserData(email,'','')
                profileData,msg = fetchuserdata.getMyProfileData()
                if(not profileData):
                    updateMyobject = UpdateMyUserobject.UpdateMyUserobject(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone,userType,planType,user_details)
                    myuser = updateMyobject.updateMyObject()
                    insertuser = InsertMyUser.InsertMyUser(email,password,firstName,lastName,address1,address2,zipcode,city,state,country,phone,user_details,userType,planType,'','')
                    msg = insertuser.insertMyNewUser()
                    return render_template("home.html",msg=msg)
                else:
                    return render_template("register.html", error="Email Id already exists",EmployeePlanName=EmployeePlanName,EmployeePlanCount=EmployeePlanCount,EmployeePlanPrice=EmployeePlanPrice,EmployeeMessagePermission=EmployeeMessagePermission,noOfPlansEmployee=noOfPlansEmployee,
                    EmployerPlanName=EmployerPlanName,EmployerPlanCount=EmployerPlanCount,EmployerPlanPrice=EmployerPlanPrice,EmployerMessagePermission=EmployerMessagePermission,noOfPlansEmployer=noOfPlansEmployer)
            else:
                return render_template("register.html", error=emailValidateFormat,EmployeePlanName=EmployeePlanName,EmployeePlanCount=EmployeePlanCount,EmployeePlanPrice=EmployeePlanPrice,EmployeeMessagePermission=EmployeeMessagePermission,noOfPlansEmployee=noOfPlansEmployee,
                EmployerPlanName=EmployerPlanName,EmployerPlanCount=EmployerPlanCount,EmployerPlanPrice=EmployerPlanPrice,EmployerMessagePermission=EmployerMessagePermission,noOfPlansEmployer=noOfPlansEmployer)
    except Exception as e:
        excep_msg = "Error in view register"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/jobs", methods = ['GET', 'POST'])
def jobs():
    try:
        if request.method == 'POST':
            jobId = request.form['jobId']
            companyName = request.form['companyName']
            title = request.form['title']
            manager = request.form['manager']
            location = request.form['location']
            jobDetails = request.form['jobDetails']
            insertjob = InsertUserJob.InsertUserJob(jobId,companyName,title,manager,location,jobDetails,session['email'],'')
            msg_1 = insertjob.insertUserJob()
            fetchjobdata = FetchMyJobData.FetchMyJobData('','')
            jobData,msg = fetchjobdata.getMyJobData()
            noOfJobs = len(jobData)
            getUserType = GetMyUserType.GetMyUserType(session['email'],'','')
            getUserTypeData,message = getUserType.getMyUserType()
            userType = getUserTypeData[2]
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            rulesEngine = RulesEngine_PlanType.RulesEngine_PlanType('')
            allowPosting,allowMessages = rulesEngine.rulesEngine_Employer(myUser.email,myUser.userType,myUser.planType)
            return render_template("jobs.html", jobData=jobData, noOfJobs=noOfJobs, msg=msg_1, jobId="Job with job id:" + jobId,allow=allowPosting,userType=userType)
    except Exception as e:
        excep_msg = "Error in view jobs"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/registerationForm")
def registrationForm():
    try:
        reader = XmlReader.XmlReader()
        EmployeePlanName,EmployeePlanCount,EmployeePlanPrice,EmployeeMessagePermission = reader.readmyFile("employee")
        noOfPlansEmployee = len(EmployeePlanName)
        EmployerPlanName,EmployerPlanCount,EmployerPlanPrice,EmployerMessagePermission = reader.readmyFile("employer")
        noOfPlansEmployer = len(EmployerPlanName)
        return render_template("register.html",EmployeePlanName=EmployeePlanName,EmployeePlanCount=EmployeePlanCount,EmployeePlanPrice=EmployeePlanPrice,EmployeeMessagePermission=EmployeeMessagePermission,noOfPlansEmployee=noOfPlansEmployee,
        EmployerPlanName=EmployerPlanName,EmployerPlanCount=EmployerPlanCount,EmployerPlanPrice=EmployerPlanPrice,EmployerMessagePermission=EmployerMessagePermission,noOfPlansEmployer=noOfPlansEmployer)
    except Exception as e:
        excep_msg = "Error in view registerform"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

##Added Error log

@app.route("/checkUserErrorLog")
def CheckErrorLog():
    try:
        text = open('Log1.log', 'r+')
        content = text.read()
        text.close()
        return render_template("Errorlog.html",content = content)
    except Exception as e:
        excep_msg = "Error in view ErrorLog"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)
##Added Error log


@app.route("/addJobs")
def addJobs():
    try:
        getUserType = GetMyUserType.GetMyUserType(session['email'],'','')
        getUserTypeData,message = getUserType.getMyUserType()
        if (getUserTypeData[2] == 'employee'):
            userType = 'employee'
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            rulesEngine = RulesEngine_PlanType.RulesEngine_PlanType('')
            allowPosting,allowMessages = rulesEngine.rulesEngine_Employer(myUser.email,myUser.userType,myUser.planType)
        else:
            userType = 'employer'
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            rulesEngine = RulesEngine_PlanType.RulesEngine_PlanType('')
            allowPosting,allowMessages = rulesEngine.rulesEngine_Employer(myUser.email,myUser.userType,myUser.planType)
        fetchjobdata = FetchMyJobData.FetchMyJobData('','')
        jobData,msg = fetchjobdata.getMyJobData()
        noOfJobs = len(jobData)
        if(noOfJobs == 0):
            return render_template("jobs.html",noOfJobs=noOfJobs,jobData=jobData,userType=userType,allow=allowPosting)
        else:
            return render_template("jobs.html", jobData=jobData, noOfJobs=noOfJobs,userType=userType,allow=allowPosting)
        if request.method == 'POST':
            email = session['email']
            insertgivenjobapplication = InsertGivenJobApplication.InsertGivenJobApplication(email,'')
            message = insertgivenjobapplication.insertGivenJobApplication()
            return render_template("jobs.html", application_msg = "",allow=allowPosting, userType=userType)
    except Exception as e:
        excep_msg = "Error in view jobs"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/addJobApplication", methods = ['GET', 'POST'])
def addJobApplication():
    try:
        if request.method == 'POST':
            email = session['email']
            getUserType = GetMyUserType.GetMyUserType(session['email'],'','')
            getUserTypeData,message = getUserType.getMyUserType()
            userType = getUserTypeData[2]
            fetchjobdata = FetchMyJobData.FetchMyJobData('','')
            jobData,msg = fetchjobdata.getMyJobData()
            insertgivenjobapplication = InsertGivenJobApplication.InsertGivenJobApplication(email,'')
            message = insertgivenjobapplication.insertGivenJobApplication()
            noOfJobs = len(jobData)
            rulesEngine = RulesEngine_PlanType.RulesEngine_PlanType('')
            allowPosting,allowMessages = rulesEngine.rulesEngine_Employer(myUser.email,myUser.userType,myUser.planType)
            return render_template("jobs.html", application_msg = message,userType=userType,jobData=jobData,noOfJobs=noOfJobs,allow=allowPosting)
    except Exception as e:
        excep_msg = "Error in view job application"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/messaging", methods = ['GET', 'POST'])
def messaging():
    try:
        if request.method == 'POST':
            #Parse form data
            recipientAddress = request.form['recipientAddress']
            mailSubject = request.form['mailSubject']
            email = session['email']
            mailBody = request.form['mailBody'] + " Sent by: " + email + " from FindMyEmployer"
            msg = Message(mailSubject, sender = email, recipients = [recipientAddress])
            msg.body = mailBody
            mail.send(msg)
            return render_template("messaging.html",msg="Message Sent!!")
    except Exception as e:
        excep_msg = "Error in view messaging"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/messageForm")
def messageForm():
    try:
        getUserType = GetMyUserType.GetMyUserType(session['email'],'','')
        getUserTypeData,message = getUserType.getMyUserType()
        if (getUserTypeData[2] == 'employee'):
            userType = 'employee'
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            rulesEngine = RulesEngine_PlanType.RulesEngine_PlanType('')
            allowPosting,allowMessages = rulesEngine.rulesEngine_Employer(myUser.email,myUser.userType,myUser.planType)
        else:
            userType = 'employer'
            fetchuserdata = FetchMyUserData.FetchMyUserData(session['email'],'','')
            profileData,msg = fetchuserdata.getMyProfileData()
            rulesEngine = RulesEngine_PlanType.RulesEngine_PlanType('')
            allowPosting,allowMessages = rulesEngine.rulesEngine_Employer(myUser.email,myUser.userType,myUser.planType)
        return render_template("messaging.html",allowMessages=allowMessages)
    except Exception as e:
        excep_msg = "Error in view messaging"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    try:
        form = UploadForm()
        name = session['email']
        if form.validate_on_submit():
            for filename in request.files.getlist('photo'):
                photos.save(filename, name=name + '.')
            success = True
        else:
            success = False
        path = app.config['UPLOADED_PHOTOS_DEST']  + "/"+ session['email']+ "/"
        if not os.path.exists(path):
            os.makedirs(path)
        for fname in os.listdir(app.config['UPLOADED_PHOTOS_DEST']):
            if fname.endswith('.jpg'):
                copyfile(app.config['UPLOADED_PHOTOS_DEST']  +"/" + name+ ".jpg", path + name+ ".jpg")
        fileUploaded = False
        if glob.glob(path + name + ".*"):
            fileUploaded = True
        files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'] +"/" +name)
        return render_template('Uploadphoto.html', form=form, success=success,files_list=files_list,fileUploaded = fileUploaded)
    except Exception as e:
        excep_msg = "Error in uploading file"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route('/open/<filename>')
def open_file(filename):
    try:
        file_url = photos.url(filename)
        return render_template('ViewImage.html', file_url=file_url)
    except Exception as e:
        excep_msg = "Error in openning file"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route('/delete/<filename>')
def delete_file(filename):
    try:
        uploaded = False
        file_path = photos.path(filename)
        os.remove(file_path)
        path = app.config['UPLOADED_PHOTOS_DEST']  + "/"+ session['email']+ "/" + filename
        os.remove(path)
        return redirect(url_for('upload_file'))
    except Exception as e:
        excep_msg = "Error in deleting file"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

@app.route("/searchProfile", methods = ['GET', 'POST'])
def searchProfile():
    try:
        if request.method == 'POST':
            #Parse form data
            searchProf = request.form['searchProf']
            if (searchProf == ''):
                return render_template("searchProfile.html",error="Enter Name to Search", noOfProfilesFetched=0)
            else:
                fetchSearchedProfile = FetchMySearchedProfile.FetchMySearchedProfile(searchProf,'','')
                fetchSearchedProfileData,msg = fetchSearchedProfile.fetchMySearchedProfile()
                noOfProfilesFetched = len(fetchSearchedProfileData)
                if (noOfProfilesFetched == 0):
                    return render_template("searchProfile.html", fetchSearchedProfileData=fetchSearchedProfileData, noOfProfilesFetched=noOfProfilesFetched,error="No Results Found")
                else:
                    return render_template("searchProfile.html", fetchSearchedProfileData=fetchSearchedProfileData, noOfProfilesFetched=noOfProfilesFetched)
    except Exception as e:
        excep_msg = "Error in view searchProfile"
        level = logging.getLogger().getEffectiveLevel()
        logmyerror.loadMyExceptionInDb(level,excep_msg,e)
        logging.info(excep_msg, exc_info=True)

if __name__ == '__main__':
    logging.basicConfig(filename='Log1.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    app.run(debug=True)
