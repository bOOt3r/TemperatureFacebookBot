import requests
import credentials as c
import dbConnect as dbc


def read_json_input(fb_input):
    user_id = fb_input["entry"][0]["messaging"][0]["sender"]["id"]

    rj_url = "https://graph.facebook.com/v11.0/" + user_id + "?access_token=" + c.pageAccessToken
    response = requests.get(rj_url, headers={"User-Agent": "curl/7.61.0"})
    json_response = response.json()

    user_first_name = json_response["first_name"]
    user_last_name = json_response["last_name"]

    dbc.save_user_to_db(user_id, user_first_name, user_last_name)

