import random
from num2words import num2words
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/question', methods=['GET'])
def get_question():
    number = random.randint(10, 100)
    correct_word = num2words(number)
    options = [correct_word]

    while len(options) < 4:
        random_number = random.randint(1, 100)
        random_word = num2words(random_number)
        if random_word not in options:
            options.append(random_word)

    random.shuffle(options)

    choices = {
        "A": options[0],
        "B": options[1],
        "C": options[2],
        "D": options[3]
    }

    question = {
        "question": f"The correct word for {number} is ________.",
        "choices": options,
        "correctAnswer": options.index(correct_word)
    }

    return jsonify(question)

if __name__ == '__main__':
    app.run()