from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the Home page'

@app.route('/passed/<sname>/<int:smarks>')
def passed(sname, smarks):
    return f"<h1>Congrats! {sname} you've passed as you got {smarks} marks</h1>"

@app.route('/fail/<sname>/<int:smarks>')
def fail(sname, smarks):
    return f"<h2>{sname.title()}, you couldn't pass the test as you got {smarks} marks, however don't be disheartened you can always try again</h2>"

@app.route('/results/<name>/<int:marks>')
def results(name, marks):
    if marks > 33: 
        return redirect(url_for('passed', sname=name, smarks=marks))
    else:
        return redirect(url_for('fail', sname=name, smarks=marks))


if __name__ == '__main__':
    app.run(debug=True)