import email
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
# This code is required to make a flask form
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[
            DataRequired(), 
            Email(message="This field requires a valid email", check_deliverability=True)],
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(),
            Length(min=8, max=30, message="Field must be at least 8 characters long."),
        ],
    )
    submit = SubmitField(label="Login")


app = Flask(__name__)
app.secret_key = "krolik"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Create and pass form to html
    form = LoginForm()
    # Validate the user's entry
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login-simplified.html", form=form)

def check_email(form):
    return 

if __name__ == "__main__":
    app.run(debug=True)
