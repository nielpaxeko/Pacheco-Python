from flask import Flask, render_template
import random 
import datetime
import requests
import json

app = Flask(__name__)

# Jinja = templating language
@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num = random_number, year = current_year)

@app.route('/guess/<name>')
def guess(name):
    # Get gender
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    genderize_response.raise_for_status
    guessed_gender = genderize_response.json()["gender"]
    # Get age
    agify_response = requests.get(f"https://api.agify.io?name={name}")
    agify_response.raise_for_status()
    guessed_age = agify_response.json()["age"]
    # Return
    return render_template("guess.html", name = name.title(), gender = guessed_gender, age = guessed_age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    with open('blog_data.json', 'r') as file:
        data = json.load(file)
    return render_template("blog.html", blog_data = data)
    
# Run the app in debug mode for auto-reload
if __name__ == "__main__":
    app.run(debug=True)