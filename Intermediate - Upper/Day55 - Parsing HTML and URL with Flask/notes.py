from flask import Flask

app = Flask(__name__)

# Advanced Decorators
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

# http://127.0.0.1:5000/username/mike/2
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello {name}, you are {number} years old!'

# Run the app in debug mode for auto-reload
if __name__ == "__main__":
    app.run(debug = True)