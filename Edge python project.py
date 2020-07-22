import bs4
import requests
from bs4 import BeautifulSoup

def get_AQI():
    r=requests.get('https://air-quality.com/place/myanmar-burma/yangon/02fe4b9d?lang=en&standard=aqi_us')
    soup=bs4.BeautifulSoup(r.text,"html")
    price= soup.find('div', {'class' : 'indexValue'}).text
    return price


print("The current AQI: " + str(get_AQI()))

for price in range(0,200):
    if price < 50:
        print("good")
        break