from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_bootstrap.forms import render_form

# Database imports
import sqlite3
from flask import Flask
import sqlalchemy as sa


""" This will install the packages from requirements.txt for this project.
pip3 install -r requirements.txt """

app = Flask(__name__)
app.config["SECRET_KEY"] = "lappland"
Bootstrap(app)

# SQLite code
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# Code for creating Table and add a book
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# Code for sqlalchemy
engine = sa.create_engine("sqlite:///new-books-collection.db")
connection = engine.connect()

metadata = sa.MetaData()

book_table = sa.Table(
    "book",
    metadata,
    sa.Column("book_id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("book_name", sa.String),
    sa.Column("book_author", sa.String),
    sa.Column("book_rating", sa.String),
)

metadata.create_all(engine)
connection = engine.connect()


def insert_book(name, author, rating):
    query = book_table.insert().values(
        book_name=name, book_author=author, book_rating=rating
    )
    connection.execute(query)
    connection.commit()


class BookForm(FlaskForm):
    book_name = StringField("Book name", validators=[DataRequired()])
    book_author = StringField("Book author", validators=[DataRequired()])
    book_rating = SelectField(
        "Book Rating",
        choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Add Book")


@app.route("/")
def home():
    query = sa.select(book_table)
    result = connection.execute(query)
    all_books = []
    for row in result:
        new_book = {
            "id": row.book_id,
            "title": row.book_name,
            "author": row.book_author,
            "rating": row.book_rating,
        }
        all_books.append(new_book)
            
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        insert_book(form.book_name.data, form.book_author.data, form.book_rating.data)
        return redirect(url_for("home"))
    else:
        return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
