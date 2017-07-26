import datetime
import calendar
from random import randint

curr_year = datetime.datetime.now().year
curr_month = calendar.month_name[datetime.datetime.now().month]
curr_day = datetime.datetime.now().day
weekday = calendar.day_name[datetime.date(curr_year, datetime.datetime.now().month, curr_day).weekday()]
curr_date = weekday + " " + curr_month + " " + str(curr_day) + ", " + str(curr_year)


def get_season():
    month = datetime.datetime.now().month
    if month == 1 or month == 2 or month == 12:
        curr_season = ["winter"]
    elif month == 3 or month == 4 or month == 5:
        curr_season = ["spring"]
    elif month == 6 or month == 7 or month == 8:
        curr_season = ["summer"]
    elif month == 9 or month == 10 or month == 11:
        curr_season = ["fall", "autumn"]
    return curr_season


def count_backwards():
    num = 100
    list = []
    while num >= 7:
        num -= 7
        list.append(str(num))
    return list


def get_random_word():
    list = []
    #file = open('/home/pi/AlzheimersIoT/Alexa/Skillsets/MemoryGame2.0/lexicon.txt', 'r')
    file = open('/usr/src/MemoryGame2.0/lexicon.txt', 'r')
    for line in file:
        line = line.strip()
        list.append(line.lower())

    rand_num = randint(0, len(list)-1)
    return list[rand_num]


remember_word = "uhh"

okay_list = ['okay', 'ok', 'OK']
season = get_season()
rand_word = get_random_word()

questionList = ["Please remember the word " + rand_word + ". Please respond with okay.",
                'What is the year?',
                'What is the season?',
                'What is the month',
                'What is the day of the week?',
                'Repeat the phrase: No ifs ands or buts',
                'Earlier I asked you to remember a word. Can you please say that word for me?',
                'Who was the first President of the United States?',
                'Spell the word WORLD backwards.'
                ]

# 'I would like you to count backward from 100 by sevens.'
# count_backwards(),

answerList = [
    okay_list,
    str(curr_year),
    season,
    curr_month,
    weekday,
    'no ifs ands or buts',
    rand_word,
    'George Washington',
    'D L R O W'
]