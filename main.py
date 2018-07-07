from flask import *

from werkzeug.utils import secure_filename
import Databaselayer
from Databaselayer import *

app = Flask(__name__)
app.secret_key = 'random string'



@app.route("/")
def root():
    if 'email' not in session:
        loggedIn = False
        firstName = ''
        return render_template('home.html',  loggedIn=loggedIn, firstName=firstName)
    else:
        loggedIn = True
        login = Databaselayer.Databaselayer_LoginClass()
        loggedIn, firstName = login.getLoginDetails_DBL(session['email'])
        return render_template("Profile2.html", loggedIn=loggedIn, firstName=firstName )


@app.route("/account/profile")
def profileHome():
    if 'email' not in session:
        return redirect(url_for('root'))
    else:
        loggedIn = True
        login = Databaselayer.Databaselayer_LoginClass()
        loggedIn, firstName = login.getLoginDetails_DBL(session['email'])
    return render_template("Profile2.html", loggedIn=loggedIn, firstName=firstName, )

@app.route("/account/profile/edit")
def editProfile():
    if 'email' not in session:
        return redirect(url_for('root'))
    login_object = Databaselayer.Databaselayer_LoginClass()
    loggedIn, firstName = login_object.getLoginDetails_DBL(session['email'])
    fetchuserdata = Databaselayer.Databaselayer_FetchUserData()
    profileData = fetchuserdata.getProfileData_DBL(session['email'])
    return render_template("editProfile.html", profileData=profileData, loggedIn=loggedIn, firstName=firstName )

@app.route("/account/profile/changePassword", methods=["GET", "POST"])
def changePassword():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    if request.method == "POST":
        oldPassword = request.form['oldpassword']
        oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
        newPassword = request.form['newpassword']
        newPassword = hashlib.md5(newPassword.encode()).hexdigest()
        changemypassword = Databaselayer.Databaselayer_ChangeMyPassword()
        msg = changemypassword.changeMyProfilePassword_DBL(session['email'],oldPassword,newPassword)
        return render_template("changePassword.html", msg=msg)
    else:
        return render_template("changePassword.html")

@app.route("/updateProfile", methods=["GET", "POST"])
def updateProfile():
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
        updatemyprofile = Databaselayer.Databaselayer_UpdateMyProfile()
        msg = updatemyprofile.updateMyProfileMethod_DBL(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
        return redirect(url_for('editProfile'))

@app.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('root'))
    else:
        return render_template('login.html', error='')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        checkifuservalid = Databaselayer.Databaselayer_CheckIfUserValid()
        value  = checkifuservalid.isValid_DBL(email, password)
        if value == True:
            session['email'] = email
            return redirect(url_for('root'))
        elif value == False:
            error = 'Invalid UserId / Password'
            return render_template('login.html', error=error)


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('root'))



@app.route("/register", methods = ['GET', 'POST'])
def register():
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
        insertuser = Databaselayer.Databaselayer_InsertUser()
        msg = insertuser.insertNewUser_DBL(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
        return render_template("login.html", error=msg)



@app.route("/registerationForm")
def registrationForm():
    return render_template("register.html")




if __name__ == '__main__':
    app.run(debug=True)
