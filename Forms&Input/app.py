from flask import Flask, render_template, url_for, redirect
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
        return redirect(url_for("home"))
    return render_template('signup.html', title='SignUp', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template('login.html', title='Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)