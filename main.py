from flask import *
from werkzeug.utils import secure_filename
import Businesslayer
from Businesslayer import *
import os.path

app = Flask(__name__)
app.secret_key = 'random string'

@app.route("/")
def root():
    try:
        if 'email' not in session:
            loggedIn = False
            firstName = ''
            return render_template('home.html',  loggedIn=loggedIn, firstName=firstName)
        else:
            loggedIn = True
            loginclassdetails = Businesslayer.Businesslayer_LoginClass()
            loggedIn, firstName = loginclassdetails.getLoginDetails_BSL(session['email'])
            return render_template("Profile2.html", loggedIn=loggedIn, firstName=firstName )
    except:
        msg = "Error in view Homepage"
        logging.info(msg, exc_info=True)

@app.route("/account/profile")
def profileHome():
    try:
        if 'email' not in session:
            return redirect(url_for('root'))
        else:
            loggedIn = True
            loginclassdetails = Businesslayer.Businesslayer_LoginClass()
            loggedIn, firstName = loginclassdetails.getLoginDetails_BSL(session['email'])
        return render_template("Profile2.html", loggedIn=loggedIn, firstName=firstName )
    except:
        msg = "Error in view profile"
        logging.info(msg, exc_info=True)

@app.route("/account/profile/edit")
def editProfile():
    try:
        if 'email' not in session:
            return redirect(url_for('root'))
        loginclassdetails = Businesslayer.Businesslayer_LoginClass()
        loggedIn, firstName = loginclassdetails.getLoginDetails_BSL(session['email'])
        fetchuserdata = Businesslayer.Businesslayer_FetchUserData()
        profileData = fetchuserdata.getProfileData_BSL(session['email'])
        return render_template("editProfile.html", profileData=profileData, loggedIn=loggedIn, firstName=firstName )
    except:
        msg = "Error in view edit profile"
        logging.info(msg, exc_info=True)

@app.route("/account/profile/changePassword", methods=["GET", "POST"])
def changePassword():
    try:
        if 'email' not in session:
            return redirect(url_for('loginForm'))
        if request.method == "POST":
            oldPassword = request.form['oldpassword']
            oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
            newPassword = request.form['newpassword']
            newPassword = hashlib.md5(newPassword.encode()).hexdigest()
            changemypassword = Businesslayer.Businesslayer_ChangeMyPassword()
            msg = changemypassword.changeMyProfilePassword_BSL(session['email'],oldPassword,newPassword)
            return render_template("changePassword.html", msg=msg)
        else:
            return render_template("changePassword.html")
    except:
        msg = "Error in view changepassword"
        logging.info(msg, exc_info=True)

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
            updatemyprofile = Businesslayer.Businesslayer_UpdateMyProfile()
            msg = updatemyprofile.updateMyProfileMethod_BSL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
            return redirect(url_for('editProfile'))
    except:
        msg = "Error in view update profile"
        logging.info(msg, exc_info=True)

@app.route("/loginForm")
def loginForm():
    try:
        if 'email' in session:
            return redirect(url_for('root'))
        else:
            return render_template('login.html', error='')
    except:
        msg = "Error in view loginform"
        logging.info(msg, exc_info=True)

@app.route("/login", methods = ['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            checkifuservalid = Businesslayer.Businesslayer_CheckIfUserValid()
            value  = checkifuservalid.isValid_BSL(email, password)
            if value == True:
                session['email'] = email
                return redirect(url_for('root'))
            elif value == False:
                error = 'Invalid UserId / Password'
                return render_template('login.html', error=error)
    except:
        msg = "Error in view login"
        logging.info(msg, exc_info=True)

@app.route("/logout")
def logout():
    try:
        session.pop('email', None)
        return redirect(url_for('root'))
    except:
        msg = "Error in view logout"
        logging.info(msg, exc_info=True)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            #Parse form data
            password = request.form['password']
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
            insertuser = Businesslayer.Businesslayer_InsertUser()
            msg = insertuser.insertNewUser_BSL(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
            return render_template("home.html", error=msg)
    except:
        msg = "Error in view register"
        logging.info(msg, exc_info=True)

@app.route("/jobs", methods = ['GET', 'POST'])
def jobs():
    try:
        if request.method == 'POST':
            #Parse form data
            jobId = request.form['jobId']
            companyName = request.form['companyName']
            title = request.form['title']
            manager = request.form['manager']
            location = request.form['location']
            jobDetails = request.form['jobDetails']
            insertjob = Businesslayer.Businesslayer_InsertJob()
            msg = insertjob.insertJob_BSL(jobId,companyName,title,manager,location,jobDetails)
            fetchjobdata = Businesslayer.Businesslayer_FetchJobData()
            jobData = fetchjobdata.getJobData_BSL('12345')
            return render_template("jobs.html", jobData=jobData)
    except:
        msg = "Error in view jobs"
        logging.info(msg, exc_info=True)

@app.route("/registerationForm")
def registrationForm():
    try:
        return render_template("register.html")
    except:
        msg = "Error in view registerform"
        logging.info(msg, exc_info=True)
		
@app.route("/addJobs")
def addJobs():
    try:
        fetchjobdata = Businesslayer.Businesslayer_FetchJobData()
        jobData = fetchjobdata.getJobData_BSL('12345')
        return render_template("jobs.html", jobData=jobData)
    except:
        msg = "Error in view jobs"
        logging.info(msg, exc_info=True)

if __name__ == '__main__':
    logging.basicConfig(filename='Log1.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger=logging.getLogger(__name__)
    app.run(debug=True)
