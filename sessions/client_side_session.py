from flask import Flask, render_template, url_for, session, redirect, flash, request
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    if "username" not in session:
        flash('Login Required')
        return redirect(url_for('Login', next=request.url))
    else:
        flash(f"Hi {session['username']}! Welcome to the app...")
    return render_template('about.html', title="About")


@app.route('/contact')
def contact():
    if "username" not in session:
        flash('Login Required')
        return redirect(url_for('Login', next = request.url))
    else:
        flash(f"Hi {session['username']}! Welcome to the app...")
    return render_template('contact.html', title='Contact')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.email.data
        flash(f"Successfully logged in as {session['username'].title()}")
        next_url = request.args.get('next')
        return redirect(next_url or url_for('home') )
    
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)