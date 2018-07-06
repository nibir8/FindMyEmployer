from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'random string'

#Seperated to different classes
class UpdateMyProfile:
    def updateMyProfileMethod(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
            with sqlite3.connect('database.db') as con:
                    try:
                        cur = con.cursor()
                        cur.execute('UPDATE users SET firstName = ?, lastName = ?, address1 = ?, address2 = ?, zipcode = ?, city = ?, state = ?, country = ?, phone = ? WHERE email = ?', (firstName, lastName, address1, address2, zipcode, city, state, country, phone, email))

                        con.commit()
                        msg = "Saved Successfully"
                    except:
                        con.rollback()
                        msg = "Error occured"
            con.close()
            return msg


class ChangeMyPassword:
    def changeMyProfilePassword(Self):
        oldPassword = request.form['oldpassword']
        oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
        newPassword = request.form['newpassword']
        newPassword = hashlib.md5(newPassword.encode()).hexdigest()
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, password FROM users WHERE email = '" + session['email'] + "'")
            userId, password = cur.fetchone()
            if (password == oldPassword):
                try:
                    cur.execute("UPDATE users SET password = ? WHERE userId = ?", (newPassword, userId))
                    conn.commit()
                    msg="Changed successfully"
                except:
                    conn.rollback()
                    msg = "Failed"
                #return render_template("changePassword.html", msg=msg)
            else:
                msg = "Wrong password"
        conn.close()
        return msg

class CheckIfUserValid:
    def isValid(Self,email, password):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT email, password FROM users')
        data = cur.fetchall()
        for row in data:
            if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
                return True
        return False

class LoginClass:
    def getLoginDetails(self):
        loggedIn = True
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, firstName FROM users WHERE email = '" + session['email'] + "'")
            userId, firstName = cur.fetchone()
        conn.close()
        return (loggedIn, firstName)

class InsertUser:
    def insertNewUser(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('INSERT INTO users (password, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, address1, address2, zipcode, city, state, country, phone))

                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return msg


class FetchUserData:
    def getProfileData(Self):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone FROM users WHERE email = '" + session['email'] + "'")
            profileData = cur.fetchone()
        conn.close()
        return profileData

@app.route("/")
def root():
    if 'email' not in session:
        loggedIn = False
        firstName = ''
        return render_template('home.html',  loggedIn=loggedIn, firstName=firstName)
    else:
        loggedIn = True
        login = LoginClass()
        loggedIn, firstName = login.getLoginDetails()
        return render_template("Profile2.html", loggedIn=loggedIn, firstName=firstName, )


@app.route("/account/profile")
def profileHome():
    if 'email' not in session:
        return redirect(url_for('root'))
    else:
        loggedIn = True
        login = LoginClass()
        loggedIn, firstName = login.getLoginDetails()
    return render_template("Profile2.html", loggedIn=loggedIn, firstName=firstName, )

@app.route("/account/profile/edit")
def editProfile():
    if 'email' not in session:
        return redirect(url_for('root'))
    login_object = LoginClass()
    loggedIn, firstName = login_object.getLoginDetails()
    fetchuserdata = FetchUserData()
    profileData = fetchuserdata.getProfileData()
    return render_template("editProfile.html", profileData=profileData, loggedIn=loggedIn, firstName=firstName )

@app.route("/account/profile/changePassword", methods=["GET", "POST"])
def changePassword():
    if 'email' not in session:
        return redirect(url_for('loginForm'))
    if request.method == "POST":
        changemypassword = ChangeMyPassword()
        msg = changemypassword.changeMyProfilePassword()
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
        updatemyprofile = UpdateMyProfile()
        msg = updatemyprofile.updateMyProfileMethod(email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
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
        checkifuservalid = CheckIfUserValid()
        value  = checkifuservalid.isValid(email, password)
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
        insertuser = InsertUser()
        msg = insertuser.insertNewUser(password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone)
        return render_template("login.html", error=msg)



@app.route("/registerationForm")
def registrationForm():
    return render_template("register.html")




if __name__ == '__main__':
    app.run(debug=True)
