# question_generator.py
import random
from num2words import num2words

def generate_question_word():
    number = random.randint(10, 100)
    correct_word = num2words(number)
    options = [correct_word]

    while len(options) < 4:
        random_number = random.randint(1, 100)
        random_word = num2words(random_number)
        if random_word not in options:
            options.append(random_word)

    random.shuffle(options)

    question = {
        "question": f"The correct word for {number} is ________.",
        "choices": options,
        "correctAnswer": options.index(correct_word)
    }

    return question

def generate_question_number():
    templates = [
        # ("The number after {num} is _______", ["A) {opt1}", "B) {opt2}", "C) {opt3}", "D) {opt4}"],),
        # ("What comes after {num}?", ["A) {opt1}", "B) {opt2}", "C) {opt3}", "D) {opt4}"]),
        ("The number after {num} is _______"),
        ("What comes after {num}?"),
    ]

    num = random.randint(10, 99)
    question_template = random.choice(templates)
    correct_answer = num + 1
    options = [correct_answer]

    while len(options) < 4:
        option = num + random.randint(1, 10)
        if option != correct_answer and option not in options:
            options.append(option)

    random.shuffle(options)

    question = question_template.format(num=num)
    # options = [option.format(opt1=options[0], opt2=options[1], opt3=options[2], opt4=options[3]) for option in question_template[1]]

    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(correct_answer)
    }

    return question_json

def question_3():
    # Generate a random number sequence
    start_number = random.randint(1, 100)
    sequence = [start_number]
    for _ in range(3):
        sequence.append(sequence[-1] + 1)
    sequence.append(sequence[-1] + 1)
    
    # Randomly select the position for the missing number
    missing_index = random.randint(1, 3)
    missing_number = sequence[missing_index]
    
    # Generate the options
    options = [missing_number]
    while len(options) < 4:
        option = random.randint(1, 100)
        if option not in options:
            options.append(option)
    
    random.shuffle(options)
    correct_answer = missing_number
    
    # Create the question and options string
    question = "Fill in the missing number.\n"
    question += ", ".join(str(num) for num in sequence[:missing_index]) + ", ______, " + ", ".join(str(num) for num in sequence[missing_index+1:])

    # Create the question JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(correct_answer)
    }

    return question_json