from flask_wtf import Form
from wtforms import StringField, PasswordField , SubmitField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(Form):
	first_name = StringField('First name',validators=[DataRequired("Please Enter your First Name")])
 	last_name = StringField('Last name',validators=[DataRequired("Please Enter your Last Name")])
 	email = StringField('Email',validators=[DataRequired("Please Enter your Email"),Email("Please Enter a valid Email Address")])
 	password= PasswordField ('Passowrd',validators=[DataRequired("Please Enter a Password"),Length(min=6,message="Passwords must be atleast 6 char long!")])
 	submit  = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email',validators=[DataRequired("Please Enter your Email-Address"),Email("Please Enter a valid Email-Address")])
	password =PasswordField ('Passowrd',validators=[DataRequired("Please Enter a Password")]) 
	submit = SubmitField("Sign In")