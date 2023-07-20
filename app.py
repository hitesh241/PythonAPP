# app.py
from flask import Flask, jsonify
from question_generator import generate_question_word, generate_question_number

app = Flask(__name__)

question_templates = [
    (generate_question_word,),
    (generate_question_number,)
]

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = [generator() for generator, in question_templates]
    return jsonify({"questions": questions})

if __name__ == '__main__':
    app.run()