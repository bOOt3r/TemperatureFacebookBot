import webScraper as ws
import fbConnect as fbc


""" 

Future implementation with greeting based on time of day.

def is_time_between(begin_time, end_time, check_time=datetime.now()):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


if (time(5, 00), time(9, 00)):
    greeting = "god morgon "

if (time(9, 00), time(12, 00)):
    greeting = "god middag  "

if (time(13, 00), time(18, 00)):
    greeting = "god eftermiddag "

elif (time(18, 00), time(5, 00)):
    greeting = "god kväll "
"""


def greet_known_user(user_id, user_first_name):
    text_to_user = "Hej igen " + user_first_name + "! Det är just nu " + ws.scrape_a_site() + " grader i vattnet."
    fbc.call_send_api(user_id, text_to_user)


def greet_new_user(user_id, user_first_name):
    text_to_user = "Hej och välkommen " + user_first_name + "! Det är just nu " + ws.scrape_a_site() + " grader i vattnet!"
    fbc.call_send_api(user_id, text_to_user)
