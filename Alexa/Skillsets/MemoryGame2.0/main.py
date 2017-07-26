import logging
from game_process_logic import *
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def process_state(user_answer):
    round = counter_dict.get("rounds")
    if round >= 5:
        message = quit_game()
        return message, 1
    if user_answer == 'yes':
        print(user_answer)
        message = yes_response()
        return message, 0
    if user_answer == 'no':
        message = quit_game()
        return message, 1
    if user_answer == 'pass':
        message = pass_response()
        return message, 0
    else:
        message = answer_response(user_answer)
        return message, 0


@ask.launch
def new_game():
    counter_dict['wins'] = 0
    counter_dict['rounds'] = 0
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("AnswerIntent", convert={'Answer': str})
def main_intent(Answer):
    user_answer = Answer
    new_msg, end = process_state(user_answer)
    if end == 0:
        return question(new_msg)
    else:
        return statement(new_msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)