from flask import Flask
from flask_ask import Ask, statement, question
app = Flask(__name__)
ask = Ask(app, '/')
#from camera import take_picture
#import matplotlib as plt
from main import main
import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
import portfolio_methods as portfolio
import match
import pickle

# run this cell to download the models from dlib
from dlib_models import download_model, download_predictor, load_dlib_models
from dlib_models import models
from camera import take_picture
import matplotlib.pyplot as plt





@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like me to take your photo?'
    download_model()
    download_predictor()
    load_dlib_models()


    return question(welcome_message)


@ask.intent("YesIntent")
def share_coin_result():
    with open("database.pkl", mode="rb") as opened_file:
        database = pickle.load(opened_file)
    name=main(database)
    if "Unknown" not in name:
        face_msg = 'Hello {}'.format(name)
        return question(face_msg+". Do you want to find your twin?")
    else:
        return question("What is your name?")


@ask.intent("NameIntent")
def assign_name(new_name):
    with open("database.pkl", mode="rb") as opened_file:
        database = pickle.load(opened_file)
    database = portfolio.create_profile(names[name], new_name, database)
    with open("database.pkl", mode="rb") as opened_file:
        database = pickle.load(opened_file)
@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Okay, goodbye'
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)