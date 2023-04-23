import requests
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36"
    }

def getWeather(city, token):
    try:
        res = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric&=lang=ru')
        data = res.json()

        # Город, Температура, Влажность, Скорость ветра
        information = [data["name"], data["main"]["temp"], data["main"]["humidity"], data["wind"]["speed"]]
        return information
    except Exception:
        return "not exist"

def parseNews(url):
    titles = []

    padge = requests.get(url, headers=headers)
    soup = BeautifulSoup(padge.text, "html.parser")

    blockTitle = soup.findAll('a', class_='list-item__title color-font-hover-only')
    for res in blockTitle:
        titles.append(res.text.strip().replace('\xa0', ' '))

    return titles

def parseJoke(url):

    padge = requests.get(url, headers=headers)
    soup = BeautifulSoup(padge.text, "html.parser")

    return soup.findAll('table', class_='text')[0].text.strip().replace('\xa0', ' ')

