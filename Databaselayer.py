import sqlite3, hashlib, os

#Seperated to different classes
class Databaselayer_UpdateMyProfile:
    def updateMyProfileMethod_DBL(Self,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
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


class Databaselayer_ChangeMyPassword:
    def changeMyProfilePassword_DBL(Self,myemail,oldPassword,newPassword):

        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, password FROM users WHERE email = '" + myemail + "'")
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

class Databaselayer_CheckIfUserValid:
    def isValid_DBL(Self,email, password):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT email, password FROM users')
        data = cur.fetchall()
        for row in data:
            if row[0] == email and row[1] == hashlib.md5(password.encode()).hexdigest():
                return True
        return False

class Databaselayer_LoginClass:
    def getLoginDetails_DBL(self,myemail):
        loggedIn = True
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, firstName FROM users WHERE email = '" + myemail + "'")
            userId, firstName = cur.fetchone()
        conn.close()
        return (loggedIn, firstName)

class Databaselayer_InsertUser:
    def insertNewUser_DBL(Self,password,email,firstName,lastName,address1,address2,zipcode,city,state,country,phone):
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


class Databaselayer_FetchUserData:
    def getProfileData_DBL(Self,myemail):
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT userId, email, firstName, lastName, address1, address2, zipcode, city, state, country, phone FROM users WHERE email = '" + myemail + "'")
            profileData = cur.fetchone()
        conn.close()
        return profileData
