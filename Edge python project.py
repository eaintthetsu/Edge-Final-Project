import bs4
import requests
from bs4 import BeautifulSoup

def get_AQI():
    r=requests.get('https://air-quality.com/place/myanmar-burma/yangon/02fe4b9d?lang=en&standard=aqi_us')
    soup=bs4.BeautifulSoup(r.text,"html")
    value= soup.find('div', {'class' : 'indexValue'}).text
    return value

def get_indicator():
    r=requests.get('https://air-quality.com/place/myanmar-burma/yangon/02fe4b9d?lang=en&standard=aqi_us')
    soup=bs4.BeautifulSoup(r.text,"html")
    indicator=soup.find('div', {'class': 'levelWrap'}).text
    return indicator



print("The Current AQI in Yangon: "+ str(get_AQI())

print("The air quality is " + "+str")