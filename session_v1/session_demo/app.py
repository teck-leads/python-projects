from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key ="random string"

# use the route '/login/' to login user

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login/', methods=["POST", "GET"])
def login():
    showform="yes"
    if request.method == 'POST':
        user = request.form['username']
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html", showform=showform)


# use the route '/user/' to get the username in the session

@app.route("/user/")
def user():
    notLoggedIn="yes"
    if "user" in session:
        user = session["user"]
        notLoggedIn='no'
        return render_template("login.html", notLoggedIn=notLoggedIn, user=user)
    else:
        return render_template("login.html", notLoggedIn=notLoggedIn)

# use the route '/logout/' to logout user
@app.route("/logout/")
def logout():
    mylogout="You've been logged out successfully!"
    logout="yes"
    session.pop("user", None)
    return render_template("logoutpage.html", logout=logout, mylogout=mylogout)

if __name__ == "__main__":
     app.run(debug=True)
    
    