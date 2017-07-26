from UploadAPI import *
from question_answer import *
from flask import render_template
from flask_ask import session
import datetime
from random import randint

year = datetime.datetime.now().year
month = datetime.datetime.now().month
current_question_list = questionList
current_answer_list = answerList
global_rand_count = int
answer_tag = ""

counter_dict = {'rounds': 0, 'wins': 0}


def yes_response():
    global answer_tag
    answer_tag = 'continue'
    message = create_next_question()
    return message


def pass_response():
    global answer_tag
    answer_tag = ''
    message = pass_question()
    return message


def answer_response(user_answer):
    global answer_tag
    answer_tag = ''
    message = check_answer(user_answer)
    return message


def quit_game():
    user = 'test_user_one'
    win = counter_dict.get('wins')
    auth_token = "fake token"
    UploadAPI(user, win, auth_token)
    message = "The game is over. You answered "\
           + str(counter_dict.get('wins')) \
           + " out of " + str(counter_dict.get('rounds'))\
           + " questions correctly. "
    return message


def create_next_question():
    global global_rand_count
    round = counter_dict.get("rounds")
    rand_round_count = randint(1, len(current_question_list) - 1)
    if round >= 5:
        return "no further questions"
    elif round == 0:
        next_question = current_question_list[0]
    else:
        next_question = current_question_list[rand_round_count]

    while next_question is None:
        rand_round_count = randint(1, len(current_question_list) - 1)
        next_question = current_question_list[rand_round_count]
    global_rand_count = rand_round_count
    current_question_list[global_rand_count] = None
    return next_question


def pass_question():
    session.attributes["previous_question"]=""
    counter_dict['rounds'] += 1
    if (counter_dict['rounds'] == 5):
        output_message = render_template('end')
    else:
        output_message = render_template('passMessage')
    return output_message


def lose():
    counter_dict['rounds'] += 1
    if (counter_dict['rounds'] == 5):
        continue_message = render_template('end')
    else:
        continue_message = render_template('lose')
    return continue_message


def win():
    counter_dict['wins'] += 1
    counter_dict['rounds'] += 1
    if (counter_dict['rounds'] == 5):
        continue_message = render_template('end')
    else:
        continue_message = render_template('win')
    return continue_message


def check_answer(user_answer):
    # TODO: REFACTOR
    global global_rand_count
    round = counter_dict.get('rounds')
    if round == 0:
        correct_answer = current_answer_list[0]
    else:
        correct_answer = current_answer_list[global_rand_count]

    if type(correct_answer) is list:
        for index in correct_answer:
            index = index.lower()
            if index == user_answer:
                message = win()
                return message
    if user_answer in correct_answer:
        message = win()
        return message
    elif len(user_answer) < len(correct_answer) or len(user_answer) > len(correct_answer):
        message = lose()
        return message
    else:
        answer_status = check_answer_status(user_answer, correct_answer)
        if answer_status == 200:
            message = win()
            return message
        else:
            message = lose()
            return message


def check_answer_status(user_answer, correct_answer):
    if user_answer == correct_answer:
        statusCode = 200
    else:
        statusCode = 400
    return statusCode
