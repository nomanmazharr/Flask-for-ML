from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    SelectField,
    PasswordField,
    DateField,
    SubmitField

)

from wtforms.validators import(
    Email,
    DataRequired,
    Optional,
    Length, 
    EqualTo
)

class SignUp(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(2,30)]
    )
    
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    gender = SelectField(
        "Gender",
        choices={"Male", "Female", "Other"}
    )

    date = DateField(
        "Date", 
        validators=[Optional()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(6,15)]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(6,15), EqualTo(password)]
    )

    submit = SubmitField(
        "Sign Up"
    )
