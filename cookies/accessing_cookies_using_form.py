from flask import Flask, render_template, url_for, make_response, redirect, flash, request
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    user = request.cookies.get('username')
    if user is None:
        flash('Login Required')
        return redirect(url_for('Login', next=request.url))
    else:
        flash(f"Hi {user}! Welcome to the app...")
    return render_template('about.html', title="About")


@app.route('/contact')
def contact():
    user = request.cookies.get('username')
    if user is None:
        flash('Login Required')
        return redirect(url_for('Login', next = request.url))
    else:
        flash(f"Hi {user}! Welcome to the app...")
    return render_template('contact.html', title='Contact')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.email.data
        response = make_response('')
        response.set_cookie('username', username)
        flash(f"Successfully logged in as {username}!")
        next_url = request.args.get('next') or url_for('home')
        response.headers["LOCATION"] = next_url
        response.status_code = 303 # redirecting user to any page 
        return response
    
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)