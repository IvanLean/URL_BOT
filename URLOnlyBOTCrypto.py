import sre_constants
import telebot
import datetime
from time import sleep
from pickle import GET
from newsapi import NewsApiClient
import requests
from googletrans import Translator
import googletrans
from bs4 import BeautifulSoup
import json
from pprint import pprint
from datetime import date

#фрагмент коннекта к новостям
newsapi = NewsApiClient(api_key='***')

def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    if root:
        article = root.select_one('article')

    return article.text



firstpart = "https://newsapi.org/v2/everything?q=Crypto&from="
secondpart = "&sortBy=popularity&apiKey=6c56cace4bdc41aab2a4832a3ef9d3f7"
current_date = date.today()
resultString = firstpart + str(current_date) + secondpart
response = requests.get(resultString)
json_response = response.text
data = json.loads(json_response)
#конец фрагмента
# Создаем экземпляр бота
bot = telebot.TeleBot('5156738496:AAEe02z02NhDCY0is9JygdO3JD4mHdRW9og')
# Функция, обрабатывающая команду /start


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Хочешь чтобы я отправил все новости про биткоин за сегодня? Введи "/get"')

@bot.message_handler(commands=["get"])
def get(m, res=False):
    for item in data['articles']:
        print(item['url'])
        bot.send_message(m.chat.id, item['url'])
        


    


# Запускаем бота
bot.polling(none_stop=True, interval=0)

