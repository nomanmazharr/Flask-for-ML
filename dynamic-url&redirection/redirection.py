from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the Home page</h1>'

# Building dynamic url
@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1>Hi {name}, How you doing? Welcome to the site. How may I help you today?</h1>'


@app.route('/pass')
def passed():
    return "<h1>Congrats! You've passed</h1>"

@app.route('/fail')
def fail():
    return "<h2>Alas! you could not pass the test however dont be disheartened let's try again</h2>"

# redirecting user according to the requirements
@app.route('/results/<int:num>')
def result(num):
    if num > 30:
        return redirect(url_for("passed"))
    else:
        return redirect(url_for("fail"))


if __name__ == '__main__':
    app.run(debug=True)
