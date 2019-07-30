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

with open("database.pkl", mode="rb") as opened_file:
    database = pickle.load(opened_file)
    #print(database["Alex"])
    print([k for k in database])
    del database["Aneesh"]
desc=None



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
    global desc
    name, desc = main(database)
    print("Desc",desc.shape )
    if "Unknown" not in name:
        face_msg = 'Hello {}'.format(name)
        return question(face_msg+". Do you want to find your twin? Say 'I want to see my twin'")
    else:
        return question("What is your name?")


@ask.intent("NameIntent")
def assign_name(name,uk,german,cogworks):
    global database
    global desc
    #print("Desc2", desc.shape)
    dbname=None
    if name is not None:
        dbname=name
    elif cogworks is not None:
        dbname=cogworks
    elif uk is not None:
        dbname=uk
    elif german is not None:
        dbname=german

    print(name,uk,german,cogworks)
    database = portfolio.create_profile(desc, dbname, database)
    return question("Do you want to find your twin? Say 'I want to see my twin'")
@ask.intent("TwinIntent")
#def search_twin():

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Okay, goodbye'
    with open("database.pkl", mode="wb") as opened_file:
        pickle.dump(database,opened_file)
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)