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

@app.route('/')
def get_all_posts():
    return render_template("index.html", blog_data=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
    return render_template("post.html", post = requested_post )

if __name__ == "__main__":
    app.run(debug=True)
