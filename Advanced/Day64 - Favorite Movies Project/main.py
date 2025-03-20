from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import sqlalchemy as sa

# On MacOS type: pip3 install -r requirements.txt
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Add Movie Form
class MovieForm(FlaskForm):
    movie_title = StringField("Movie title", validators=[DataRequired()])
    movie_year = StringField("Release Date", validators=[DataRequired()])
    movie_description = StringField("Description")
    movie_rating = FloatField( "Movie Rating")
    movie_ranking = StringField("Ranking")
    movie_review = StringField("My review")
    movie_url = StringField("Link to Movie")
    submit = SubmitField("Add Movie")
# Edit movie
class EditForm(FlaskForm):
    movie_rating = FloatField("Your rating out of 10")
    movie_ranking = StringField("Your review")
    submit = SubmitField("Edit Movie")


# CREATE DB
engine = sa.create_engine("sqlite:///favorite-movies.db")
connection = engine.connect()
metadata = sa.MetaData()

# CREATE TABLE
movies_table = sa.Table(
    "movies",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("title", sa.String, unique=True, nullable=False),
    sa.Column("year", sa.Integer),
    sa.Column("description", sa.String),
    sa.Column("rating", sa.Float),
    sa.Column("ranking", sa.Integer),
    sa.Column("review", sa.String),
    sa.Column("img_url", sa.String),
)
metadata.create_all(engine)
connection = engine.connect()

# Add movies to db
def insert_movie(title, year, description, rating, ranking, review, img_url):
    query = movies_table.insert().values(
        title=title, 
        year=year, 
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url,
    )
    connection.execute(query)
    connection.commit()


@app.route("/")
def home():
    query = sa.select(movies_table).order_by(movies_table.c.ranking)
    result = connection.execute(query)
    all_movies = []
    for row in result:
        new_movie = {
            "id": row.id,
            "title": row.title,
            "year": row.year,
            "description": row.description,
            "rating": row.rating,
            "ranking": row.ranking,
            "review": row.review,
            "img_url": row.img_url,
        }
        all_movies.append(new_movie)
            
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods = ["GET", "POST"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        insert_movie(
            form.movie_title.data, 
            form.movie_year.data, 
            form.movie_description.data, 
            form.movie_rating.data,
            form.movie_ranking.data,
            form.movie_review.data,
            form.movie_url.data,
        )
        return redirect(url_for("home"))
    else:
        return render_template("add.html", form=form)

@app.route("/edit/<string:movie_title>", methods=["GET", "POST"])
def edit(movie_title):
    form = EditForm()
    if form.validate_on_submit():
        new_rating = form.movie_rating.data
        new_review = form.movie_ranking.data
        query = movies_table.update().where(movies_table.c.title == movie_title).values(rating=new_rating, review=new_review)
        connection.execute(query)
        connection.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie_title=movie_title)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    query = movies_table.delete().where(movies_table.c.id == movie_id)
    connection.execute(query)
    connection.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
