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
    question = "Fill in the missing number.\\n\\n"
    question += ", ".join(str(num) for num in sequence[:missing_index]) + ", ______, " + ", ".join(str(num) for num in sequence[missing_index+1:])

    # Create the question JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(correct_answer)
    }

    return question_json

def question_4():
    tens = random.randint(1, 9)  # Generate a random number for the tens digit (between 1 and 9)
    ones = random.randint(1, 10)  # Generate a random number for the ones digit (between 1 and 10)

    answer = tens * 10 + ones  # Calculate the correct answer

    # Generate random incorrect options by adding/subtracting random values to/from the answer
    options = [answer]
    while len(options) < 4:
        option = random.randint(answer - 20, answer + 20)
        if option != answer and option not in options and option > 0:
            options.append(option)

    random.shuffle(options)  # Randomly shuffle the options

    # Create the question and the answer options
    question = f"{tens} tens and {ones} ones = _____"

    # Create the question and options JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(answer)
    }

    return question_json

def question_5():
    number = random.randint(10, 99)
    tens = number // 10
    ones = number % 10
    
    options = [
        f"{tens} tens + {ones} ones",
        f"{random.randint(1, 9)} tens + {random.randint(1, 9)} ones",
        f"{random.randint(1, 9)} tens + {random.randint(1, 9)} ones",
        f"{random.randint(1, 9)} tens + {random.randint(1, 9)} ones"
    ]
    random.shuffle(options)
    
    correct_option = options.index(f"{tens} tens + {ones} ones")
    
    question = f"How many tens and ones in {number}?\n"
    
    # Create the question and options JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": correct_option
    }

    return question_json

def question_6():
    words = ["INDIA", "UNITED", "AUSTRALIA", "BRAZIL", "CANADA", "GERMANY", "EGYPT", "FRANCE", "JAPAN", "ITALY",
             "ARGENTINA", "MEXICO", "CHINA", "RUSSIA", "SPAIN", "SWEDEN", "THAILAND", "TURKEY", "UKRAINE", "VIETNAM"]

    letters = ["I", "D", "A", "B", "C", "G", "E", "F", "J", "L",
               "N", "M", "H", "R", "S", "W", "T", "U", "K", "V"]

    word = random.choice(words)
    letter = random.choice(letters)

    # Count the number of occurrences of the letter in the word
    count = word.count(letter)

    # Regenerate options if count is zero
    while count == 0:
        word = random.choice(words)
        count = word.count(letter)

    # Generate unique random options
    options = [count]
    while len(options) < 4:
        random_count = random.randint(1, len(word))
        if random_count not in options:
            options.append(random_count)

    # Shuffle the options
    random.shuffle(options)

    # Create the question and answer options
    question = f"How many times does the letter '{letter}' appear in the word '{word}'?"
    answer_options = {
        "A": options[0],
        "B": options[1],
        "C": options[2],
        "D": options[3]
    }

    answer_options_string = "\n".join([f"{key}) {value}" for key, value in answer_options.items()])

    # Create the question and options JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(count)
    }

    return question_json

def question_7():
    number = random.randint(1, 99)  # Generate a random number

    correct_option = number + 1  # The correct option is the number incremented by 1

    options = [correct_option]
    while len(options) < 4:
        random_number = random.randint(1, 100)
        if random_number not in options:
            options.append(random_number)

    # Shuffle the options including the correct option
    random.shuffle(options)

    question = f"______ comes after {number}."

    # Create the question and options JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(correct_option)
    }

    return question_json

def question_13():
    skip_value = random.randint(2, 9)
    missing_position = random.randint(3, 5)  # Position of the missing term
    missing_term = missing_position * skip_value

    options = [missing_term]  # Start with the missing term as the first option
    while len(options) < 4:
        option = random.randint(1, 10) * skip_value
        if option not in options:
            options.append(option)

    random.shuffle(options)

    question = f"Skip by {skip_value}.\n"
    for i in range(1, 6):
        if i == missing_position:
            question += "________, "
        else:
            question += f"{i * skip_value}, "
    question = question.rstrip(", ")  # Remove the trailing comma and whitespace

    answer_options = "A) {} \nB) {}\nC) {}\nD) {}\n".format(*options)
    answer = chr(ord('a') + options.index(missing_term))

    # Create the question and options JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(missing_term)
    }

    return question_json

def question_15():
    # Generate a random number sequence
    start_number = random.randint(1, 100)
    sequence = [start_number]
    increment = random.randint(2, 9)  # Random increment value between 2 and 9
    for _ in range(3):
        sequence.append(sequence[-1] + increment)
    sequence.append(sequence[-1] + increment)
    
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
    
    # Create the question and options string
    question = "Fill in the missing number.\n"
    question += ", ".join(str(num) for num in sequence[:missing_index]) + ", ______, " + ", ".join(str(num) for num in sequence[missing_index+1:])
    
    # Create the question and options JSON
    question_json = {
        "question": question,
        "choices": options,
        "correctAnswer": options.index(missing_number)
    }

    return question_json