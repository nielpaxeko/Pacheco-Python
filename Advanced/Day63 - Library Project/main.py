from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_bootstrap.forms import render_form 

""" This will install the packages from requirements.txt for this project.
pip3 install -r requirements.txt """

app = Flask(__name__)
app.config["SECRET_KEY"] = "lappland"
Bootstrap(app)


class BookForm(FlaskForm):
    book_name = StringField("Book name", validators=[DataRequired()])
    book_author = StringField("Book author", validators=[DataRequired()])
    book_rating = SelectField(
        "Book Rating",
        choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Add Book")
all_books = []


@app.route('/')
def home():
    return render_template("index.html", books = all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = {
            "book_name": form.book_name.data,
            "book_author": form.book_author.data,
            "book_rating": form.book_rating.data
        }
        all_books.append(new_book)
        return redirect(url_for("home"))
    else:
        return render_template("add.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)

