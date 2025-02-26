from flask import Flask
import random

app = Flask(__name__)
RANDOM_NUMBER = random.randint(1, 10)
print(RANDOM_NUMBER)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 1 and 100</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<int:guess>")
def check_answer(guess):
    global RANDOM_NUMBER 
    if guess == RANDOM_NUMBER:
        return "<h1>YOU GOT IT RIGHT</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"
    elif guess > RANDOM_NUMBER:
        return "<h1>TOO HIGH, TRY AGAIN</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"
    elif guess < RANDOM_NUMBER:
        return "<h1>TOO LOW, TRY AGAIN</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"
    

# Run the app in debug mode for auto-reload
if __name__ == "__main__":
    app.run(debug=True)
