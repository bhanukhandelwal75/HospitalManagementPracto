from flask import Flask ,render_template,url_for,session,redirect,request
import pymysql
app=Flask(__name__)
app.secret_key="super secret key"

@app.route("/")
def loginx():
    return render_template('firstbootstrap.html')




@app.route("/loginpage",methods=['GET','POST'])
def loginpage():
    if(request.method=='POST'):
        email = request.form['t1']  # T1 is name of textfield
        password = request.form['t2']

        print(email,password)
        con = pymysql.connect(host="localhost",
                              port=3307,
                              db="finalproject",
                              user="root",
                              passwd="",
                              autocommit=True)

        cur=con.cursor()
        sql="select * from finalproject where email='"+email+"' and password='"+password+"'"

        
        cur.execute(sql)
        n = cur.rowcount
        print(n)
        if (n == 1):
            row = cur.fetchone()
            usertype = row[2]

            session["usertype"] = usertype
            session["email"] = email
            # adminhospital and userhospital and loginwsecurity projecthospital auth_error
            if (usertype == "admin"):
                return redirect(url_for("adminhospitals"))  # .html is not use because of function
            if (usertype == "doctor"):
                return redirect(url_for("doctor"))  # redirect=when function and render when html is used
            if (usertype == "reception"):
                return redirect(url_for("reception"))
            if (usertype == "patient"):
                return redirect(url_for("patient"))

        else:
            return render_template("loginerror.html")

    else:
        return render_template("loginpage.html")


#weare making the analogous component of permission_denied which show when backed
@app.route("/permission_denied")
def permission_denied ():
    return render_template("permission_denied.html")


@app.route("/adminhospitals" ,methods=['GET' ,'POST'] )
def adminhospitals():
    return render_template('adminhospitals.html')

@app.route("/doctor")
def doctor():
    return render_template('doctor.html')

@app.route("/reception")
def reception():
    return render_template('reception.html')

@app.route("/patient")
def patient():
    return render_template('patient.html')





#IT IS SHOWING  DOCTOR DATA, DOCTORS

@app.route("/doctorschedule")
def doctorschedule():
    if "usertype" in session:
        usertype = session["usertype"]
        email = session["email"]
        if usertype == "doctor":
            con = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)

            cur = con.cursor()
            sql="select * from doctordata "
            cur.execute(sql)
            n = cur.rowcount
            ms = "value successfully  not registered"
            if (n>0):
                data=cur.fetchall()

                return render_template("doctorschedule.html", d=data )
            else:
                return render_template("doctorschedule.html" ,ms=ms)
        else:
            return render_template("doctorschedule.html" )
    else:
        return redirect(url_for("permission_denied"))

#THIS IS DOCTOR REGISTER AREA
@app.route('/doctordetails',methods=['GET' ,'POST'])
def doctordetails():
    if "usertype" in session:
        usertype = session["usertype"]
        email = session["email"]
        if usertype == "doctor":


            if request.method == 'POST':
                docname = request.form["A1"]
                specialist=request.form["A2"]
                sittinghours =request.form["A3"]
                address=request.form["A4"]
                days=request.form["A5"]
                email=request.form['A6']
                fees=request.form['A7']
                Experience=request.form['A8']
                photo=request.form['A9']
                docid=request.form['A10']
                con = pymysql.connect(host="localhost",
                                      port=3306,
                                      user="root",
                                      db="finalproject",
                                      passwd="",
                                      autocommit=True)



                cur=con.cursor()
                sql="insert into doctordata values('"+docname+"','"+specialist+"','"+sittinghours+"', '"+address+"','"+days+"','"+email+"' ,'"+fees+"','"+Experience+"' ,'"+photo+"','"+docid+"' )"
                cur.execute(sql)
                n=cur.rowcount
                ts="data not saved"


                if n==1:
                    ts="data save sucesfully"
                return render_template("doctordetails.html", ts=ts)
            else:
                return render_template("doctordetails.html")
        else:
            return render_template("doctordetails.html")
    else:
        return redirect(url_for("permission_denied"))

#THIS IS LOGOUT  PAGE
@app.route("/logout")
def logout():

    if "usertype" in session:
        session.pop("usertype",None)
        session.pop("email",None)
        return redirect(url_for("loginx"))
    else:
        return redirect(url_for("loginx"))




#for patient: FOR CONSULT DOCTOR PAGE (imp)







@app.route("/page3",methods=['GET' ,'POST'])
def consultdoctor ():
    return render_template("page3.html")


@app.route("/paymentlink")
def paymentlink ():
    return render_template("paymentlink.html")



@app.route("/editservices",methods=['GET' ,'POST'])
def editservices():
    if "usertype" in session:


        if request.method == 'POST':
            con = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)
            sp= request.form['A2']
            cur=con.cursor()
            sql="select * from doctordata where specialist='"+sp+"'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "data not saved"
            if (n>0):
                data = cur.fetchall()

                return render_template("editservices.html",d=data )
            else:
                return render_template("editservices.html",ms=ms )
        else:
            return render_template("editservices.html")
    else:
        return redirect(url_for("permission_denied"))




@app.route("/patientfile",methods=['GET' ,'POST'])
def patientfile():
    if "usertype" in session:


        if request.method == 'POST':
            con = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)
            date= request.form['T6']
            cur=con.cursor()
            sql="select * from patient where appointmentdate='"+date+"'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "no appointments"
            if (n>0):
                data = cur.fetchall()

                return render_template("patientfile.html",d=data )
            else:
                return render_template("patientfile.html",ms=ms )
        else:
            return render_template("patientfile.html")
    else:
        return redirect(url_for("permission_denied"))






@app.route("/bookedata",methods=['GET' ,'POST'])
def bookedata():
    if "usertype" in session:


        if request.method == 'POST':
            con = pymysql.connect(host="localhost",
                                  port=3307,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)
            date= request.form['T6']
            cur=con.cursor()
            sql="select * from patient where appointmentdate='"+date+"'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "no appointments"
            if (n>0):
                data = cur.fetchall()

                return render_template("bookedata.html",d=data )
            else:
                return render_template("bookedata.html",ms=ms )
        else:
            return render_template("bookedata.html")
    else:
        return redirect(url_for("permission_denied"))



@app.route('/signup',methods=['GET' ,'POST'])
def signup():
    if (request.method == 'POST'):
        email = request.form["A1"]
        password = request.form["A2"]

        usertype = request.form["A4"]

        con = pymysql.connect(host="localhost",
                              port=3307,
                              user="root",
                              db="finalproject",
                              passwd="",
                              autocommit=True)

        cur = con.cursor()
        sql = "insert into finalproject values('" + email + "','" + password + "', '" + usertype + "' )"
        cur.execute(sql)
        n = cur.rowcount
        ts = "dont saved"

        if n == 1:
            ts = "Login now"
        return render_template("signup.html", ts=ts)

    else:
        return render_template("signup.html")

#bill code
@app.route('/showbill',methods=['GET' ,'POST'])
def showbill():
    if "usertype" in session:


        if request.method == 'POST':
            docid = request.form["H1"]
            con = pymysql.connect(host="localhost",
                                  port=3307,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)


            cur = con.cursor()
            sql = "select * from mybill where docid='" + docid+ "'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "FEES NOT PAID"
            if(n>0):
                sata = cur.fetchall()

                return render_template("showbill.html", sata=sata)
            else:
                return render_template("showbill.html", ms=ms)
        else:
            return render_template("showbill.html")
    else:
        return redirect(url_for("permission_denied"))





@app.route('/sendbill',methods=['GET' ,'POST'])
def sendbill():
    if "usertype" in session:


        if request.method == 'POST':
            docid = request.form["H1"]
            con = pymysql.connect(host="localhost",
                                  port=3307,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)


            cur = con.cursor()
            sql = "select * from mybill where docid='" + docid+ "'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "FEES NOT PAID"
            if(n>0):
                sata = cur.fetchall()

                return render_template("showbill.html", sata=sata)
            else:
                return render_template("showbill.html", ms=ms)
        else:
            return render_template("showbill.html")
    else:
        return redirect(url_for("permission_denied"))







@app.route('/bookdoctor',methods=['GET' ,'POST'])
def bookdoctor():
    if "usertype" in session:


        if request.method == 'POST':
            con = pymysql.connect(host="localhost",
                                  port=3307,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)
            sp= request.form['A2']
            cur=con.cursor()
            sql="select * from doctordata where specialist='"+sp+"'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "data not saved"
            if (n>0):
                data = cur.fetchall()

                return render_template("bookdoctor.html",d=data )
            else:
                return render_template("bookdoctor.html",ms=ms )
        else:
            return render_template("bookdoctor.html")
    else:
        return redirect(url_for("permission_denied"))


@app.route('/patientbook',methods=['GET' ,'POST'])
def patientbook():
    if "usertype" in session:



        if request.method == 'POST':
            docid = request.form["L10"]
            con = pymysql.connect(host="localhost",
                                  port=3307,
                                  user="root",
                                  db="finalproject",
                                  passwd="",
                                  autocommit=True)


            cur = con.cursor()
            sql = "select * from doctordata where docid='" + docid+ "'"
            cur.execute(sql)
            n = cur.rowcount
            ms = "return back"
            if(n>0):
                data = cur.fetchall()

                return render_template("patientbook.html", data=data)
            else:
                return render_template("patientbook.html", ms=ms)
        else:
            return render_template("patientbook.html")
    else:
        return redirect(url_for("permission_denied"))


@app.route("/page18",methods=['GET' ,'POST'])
def page18():
    if "usertype" in session:
        usertype = session["usertype"]
        email = session["email"]
        if usertype == "patient":


            if request.method == 'POST':

                name = request.form["T1"]
                mobno=request.form["T2"]
                address =request.form["T3"]
                email=request.form["T4"]
                symptoms=request.form["T5"]
                appointmentdate = request.form["T6"]
                slot = request.form["time"]
                #docid=request.form["T7"]

                con = pymysql.connect(host="localhost",
                                      port=3307,
                                      user="root",
                                      db="finalproject",
                                      passwd="",
                                      autocommit=True)



                cur=con.cursor()
                sql="insert  into patient values(0,'"+name+"','"+mobno+"','"+address+"', '"+email+"','"+symptoms+"','"+appointmentdate+"','"+slot+"','"+doctor_email+"',0)"
                cur.execute(sql)
                n=cur.rowcount
                ts="data not saved"
                if n==1:
                    ts="register successfully and click here to go card details"
                return render_template("patientbook.html", ts=ts )
            else:
                return render_template("patientbook.html")
        else:
            return render_template("patientbook.html")
    else:
        return redirect(url_for("permission_denied"))




if __name__ == "__main__":
    app.run(debug=True)




