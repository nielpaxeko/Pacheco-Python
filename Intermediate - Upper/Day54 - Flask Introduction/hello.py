from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# Run code through terminal instead of flask run
if __name__ == "__main__":
    app.run()