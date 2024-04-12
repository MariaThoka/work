from flask import Flask,render_template,request,redirect,url_for, flash
app = Flask (__name__)
import sqlite3
import os

cd=os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ACCOUNT.html")
def account():
    return render_template("ACCOUNT.html")

@app.route("/ACCOUNT.html",  methods=['POST'])
def getvalue():
    if request.method=='POST':
        connection=sqlite3.connect(cd + "/userdata.db")
        curr=connection.cursor()

        email=request.form['email']
        password=request.form['password']

        query ="SELECT email,password FROM details where email='"+email+"' and password='"+password+"'"
        curr.execute(query)
        results= curr.fetchall()
        if len(results)==0:
            failed="SORRY! ACCOUNT NOT RECOGNIZED..TRY AGAIN"
            return render_template("/ACCOUNT.html",fail=failed) 
        else:
            render_template("/ORDER ONLINE.html")



    

    return render_template("/ORDER ONLINE.html", )


@app.route("/ABOUT.html")
def about():
    return render_template("ABOUT.html")

@app.route("/SHOP.html")
def shop():
    return render_template("SHOP.html")

@app.route("/ORDER ONLINE.html")
def order():
    return render_template("ORDER ONLINE.html")

@app.route("/orderoutput.html",  methods=['POST'])
def get():
    email = request.form['EMAIL']
    number = request.form['number']
    muffins = request.form['muffins']
    payment = request.form['payment']

    connection = sqlite3.connect(cd + "/userdata.db")
    curr=connection.cursor()
    curr.execute("INSERT INTO details2(muffin,number,email,payment) VALUES(?,?,?,?)",(muffins,number,email,payment))
    connection.commit()

    return render_template("orderoutput.html",muffin=muffins,email=email,payment=payment,number=number)
    


@app.route("/OURLOCATION.html")
def location():
    return render_template("OURLOCATION.html")

@app.route("/CONTACT.html")
def contact():
    return render_template("CONTACT.html")

@app.route("/signup.html")
def sign():
    return render_template("signup.html")

@app.route("/signupoutput.html",  methods=['POST'])
def signin():
    email = request.form['email']
    number = request.form['phone number']
    password = request.form['password']
    username = request.form['username']

    connection = sqlite3.connect(cd + "/userdata.db")
    curr=connection.cursor()
    curr.execute("INSERT INTO details(username,password,email,phonenumbers) VALUES(?,?,?,?)",(username,password,email,number))
    connection.commit()

    return render_template("signupoutput.html",name=username)




    

if __name__ == "__main__":
    app.run(debug=True)