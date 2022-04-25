import dbConnect as dbc
import requests
from bs4 import BeautifulSoup


def scrape_a_site():

    url = ""
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    temp_text = soup.find(id="temp1")
    temp = temp_text.text[:-2]
    dbc.save_temperature_to_db(temp)

    return temp


