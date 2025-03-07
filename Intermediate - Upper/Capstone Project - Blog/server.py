from flask import Flask, render_template, request
import json
from post import Post
import smtplib
from dotenv import load_dotenv
import os
# Load environment variables from the .env file
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD =  os.getenv("PASSWORD")

with open("blog_data.json", "r") as file:
    posts = json.load(file)
    post_objects = []
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", blog_data=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= f"Subject: Testing\n\n{email_message}"
        )


@app.route("/post/<int:post_id>")
def post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
