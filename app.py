from flask import Flask, jsonify
from flask_cors import CORS
from question_generator import generate_question_word, generate_question_number, question_3, question_4

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for the entire app

question_templates = [
    (generate_question_word,),
    (generate_question_number,),
    (question_3,),
    (question_4,)
]

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = [generator() for generator, in question_templates]
    return jsonify({"questions": questions})

if __name__ == '__main__':
    app.run()