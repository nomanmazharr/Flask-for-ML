from flask import Flask, render_template, url_for, redirect, flash
from form import SignUp, Login

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        flash(f"Successfully registered {form.username.data}")
        return redirect(url_for("home"))
    return render_template('signup.html', title='SignUp', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if email == "Ali@gmail.com" and password == '123456':
            flash("Successfully LoggedIn")
            return redirect(url_for('home')) 
        else:
            flash("Incorrect Email or Password") 
    return render_template('login.html', title='Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)