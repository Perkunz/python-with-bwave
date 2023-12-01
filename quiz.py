import random

#global variables

questions = [
    ('What is the capital of Nigeria?', 'Abuja'),
    ('Which planet is known as the red planet?', 'Mars'),
    ('What is the largest animal in the world?', 'Blue Whale'),
    ('In which year did the Titanic sank?', '1912'),
    ('What is the square root of 81?', '9'),
]


#FUNCTION TO SHUFFLE THE QUESTION
def shuffle_questions():
    random.shuffle(questions)


#Function to conduct the quiz
def conduct_quiz():
    score = 0

    for question, answer in questions:

        user_answer = input(f'{question} ')

        if user_answer.lower() == answer.lower():
            print('Correct!!! \n')
            score += 1
        else:
            print(f'Wrong Answer! The correct answer is {answer}. \n')


            print(f'Quiz Completed. Your score is: {score}/{len(questions)}')


shuffle_questions() #
conduct_quiz() #