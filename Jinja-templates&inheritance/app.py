from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/employees')
def employees():
    return render_template('employees.html', title='Employees')


@app.route('/managers')
def managers():
    return render_template('manager.html', title='Managers')

if __name__ == '__main__':
    app.run(debug=True)