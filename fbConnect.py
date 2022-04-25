import requests
import credentials as cr


def call_send_api(user_id, text_to_user):
    response = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": f"{text_to_user}",
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "https://www.klart.se/se/hallands-l%C3%A4n/v%C3%A4der-skrea-strand/",
                        "title": "Väderprognos"
                    },
                    {
                        "type": "web_url",
                        "url": "https://open.spotify.com/show/0cGDX2zVoospthKjPmJjdJ?si=8aljF9PERbSYAH3SiOTzIQ",
                        "title": "Lyssna på en pod",
                    },
                    {
                        "type": "postback",
                        "payload": "button1",
                        "title": "Kolla igen"
                    }

                ]
            }
        }
    }
    payload = {
        "recipient": {"id": user_id},
        "message": response,
    }
    headers = {"content-type": "application/json"}

    url = "https://graph.facebook.com/v2.6/me/messages?access_token=" + cr.pageAccessToken
    r = requests.post(url, json=payload, headers=headers)
#    print(r.text)
