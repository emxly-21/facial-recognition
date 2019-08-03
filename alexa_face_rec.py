from flask import Flask
from main2 import main
import pickle
import portfolio_methods as portfolio
from fortune_cookie_fortune_teller import generator

from flask_ask import Ask, question, statement, session
app = Flask(__name__)
ask = Ask(app, "/")

current_dict = None


@ask.launch
def launch_app():
    global current_dict
    names, name, desc = main()
    current_dict = names
    if isinstance(names, dict):
        for name in names:
        # updates or creates a profile
            if "Unknown" not in name:
                namereturn = name
                session.attributes["current_person"] = namereturn

                return question("You are" + namereturn + ", right?")
            else:
                return question("Hello, what is your name?")
    else:
        return question(names)

@ask.intent("CorrectNameIntent")
def correct():
    global current_dict
    name = session.attributes["current_person"]
    names = current_dict
    with open("database.pkl", mode="rb") as opened_file:
        database = pickle.load(opened_file)
    database = portfolio.update_profile(names[name], name, database)
    with open("database.pkl", mode="wb") as opened_file:
        pickle.dump(database, opened_file)

    return question("Hello " + name + ", would you like to hear your fortune?")

@ask.intent("FindNameIntent")
def find_name(newname):
    names, name, desc = main()
    if isinstance(names, dict):
        with open("database.pkl", mode="rb") as opened_file:
            database = pickle.load(opened_file)
        if newname in database:
            database = portfolio.update_profile(names[name], newname, database)
        else:
            database = portfolio.create_profile(names[name], newname, database)
        with open("database.pkl", mode="wb") as opened_file:
            pickle.dump(database, opened_file)
        session.attributes["current_person"] = newname
        return question("Okay. Hello " + newname + " would you like to hear your fortune?")
    else:
        return question("Please look in the camera and say your name again")

@ask.intent("WrongNameIntent")
def wrong_name():
    return question("My bad, what is your name?")

@ask.intent("FortuneIntent")
def give_fortune():
    my_fortune = generator.tell_fortune()
    strig= " ." * 100
    session.attributes["current_fortune"] = my_fortune
    return question(my_fortune + strig + "If you want to save this fortune say: Save")


fortune_dict = {}
@ask.intent("SaveIntent")
def save_fortune():
    name = session.attributes["current_person"]
    my_fortune = session.attributes["current_fortune"]

    fortune_dict[name] = my_fortune
    print(fortune_dict)
    with open("save_fortune.pkl", mode="wb") as opened_file:
        pickle.dump(fortune_dict, opened_file)
    return statement("Its saved!")

@ask.intent("ShowSavedIntent")
def show_saved():
    name = session.attributes["current_person"]
    with open("save_fortune.pkl", mode="rb") as opened_file:
        saved_fortunes = pickle.load(opened_file)
    previous_fortune = saved_fortunes[name]

    return statement(previous_fortune)

@ask.intent("AMAZON.CancelIntent")
def bye():
    return statement("Goodbye")

if __name__ == '__main__':

    app.run(debug=True)