from flask import Flask, make_response, request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'

@app.route('/')
@app.route('/home')
def home():
    response = make_response("Welcome to the Home Page!")
    return response

@app.route('/set-cookie')
def set_cookie():
    response = make_response("<h1> Set your cookies value on this page... <h1/>")
    response.set_cookie('Cookie_for_user', 'Bilal') # we can change the name and set cookie by refreshing the page for the user we enter
    return response

@app.route('/get-cookie')
def get_cookie():
    user_name = request.cookies.get('Cookie_for_user')
    response = make_response(f"<h1>Here you can check the cookie that you send... <h1/>Cookie has been generated for user {user_name}")

    return response


if __name__ == '__main__':
    app.run(debug=True)