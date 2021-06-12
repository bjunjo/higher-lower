from flask import Flask
import random

# Create a new Flask application where the home route displays an
# <h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com
app = Flask(__name__)

@app.route("/")
def guess_a_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


# Generate a random number between 0 and 9 or any range of numbers of your choice.
correct_answer = random.randint(0, 9)
print(f"Answer: {correct_answer}")

# Create a route that can detect the number entered by the user
# e.g "URL/3" or "URL/9" and checks that number against the generated random number.
@app.route("/<user_answer>")
def hints(user_answer):
    # If the number is too low, tell the user it's too low,
    if int(user_answer) < correct_answer:
        return '<h1 style="color: blue">It\'s too low</h1> ' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    # same with too high or if they found the correct number. try to make the <h1> text a different colour for each page
    elif int(user_answer) > correct_answer:
        return '<h1 style="color: red">It\'s too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    else:
        return '<h1>That\'s right</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'

if __name__ == "__main__":
    app.run(debug=True)