from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Welcome to Home page</h1>'


@app.route('/about')
def about():
    return '<h1>this is my about page</h1>'

# Passing name as parameter to the Url
@app.route('/contact/<name>')
def welcome(name):
    return f'Hi {name}, welcome to my website'


# taking number as input in url
@app.route('/addition/<int:num>')
def addition(num):
    return f'Input is {num} and output is {num*5}'

# Taking two numbers as input and adding them
@app.route('/2inputs/<int:num1>/<int:num2>')
def add_two_number(num1, num2):
    return f'Sum of {num1} and {num2} is {num1+num2}'


if __name__== '__main__':
    print('starting flask app')
    app.run(debug=True)