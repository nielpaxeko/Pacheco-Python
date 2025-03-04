from flask import Flask, render_template
import json
from post import Post

with open("blog_data.json", "r") as file:
        posts = json.load(file)
        post_objects = []
        for post in posts:
            post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
            post_objects.append(post_obj)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", blog_data=post_objects)

@app.route("/post/<int:id>")
def read_post(id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            requested_post = blog_post
    return render_template("post.html", post = requested_post )

if __name__ == "__main__":
    app.run(debug=True)
