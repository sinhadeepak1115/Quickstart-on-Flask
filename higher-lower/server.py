from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess the number between 0 to 9</h1>"

no = random.randint(0, 9)
print(no)

@app.route("/<int:guess>")
def check_guess(guess):
    if guess == no:
        return "<h1 style='color: red'>You Got It.</h1>"\
               "<img src='https://media.giphy.com/media/Z8YzheiCool0I/giphy.gif'/>"

    elif guess > no:
        return "<h1 style='color: red'>Too high, try again!</h1>"\
                "<img src='https://media.giphy.com/media/d28l49Itft5kI/giphy.gif'/>"
    else:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
                "<img src='https://media.giphy.com/media/SHe9EO6PEB8L6/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)

