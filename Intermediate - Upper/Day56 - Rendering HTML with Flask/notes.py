# This lesson shows how to render html files using flask
# ALL HTML FILES MUST BE LOCATED IN A FOLDER CALLED TEMPLATES
# ALL CSS FILES MUST BE LOCATED IN A FOLDER CALLED STATIC
# The render_template import is necessary to achieve this
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def load():
    return render_template("angela.html")



# Run the app in debug mode for auto-reload
if __name__ == "__main__":
    app.run(debug=True)