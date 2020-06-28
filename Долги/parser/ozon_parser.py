import re #отвечает за регулярные выражения
import requests #библиотека, которая у нас отвечает за веб запросы
from user_agent import generate_user_agent
from bs4 import BeautifulSoup #просто парсер
import urllib3
import os #Для создания папок

headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
page = requests.get('https://www.ozon.ru/highlight/38208/', timeout=5, headers=headers)
name_folder = input("Введите название папки: \n")
os.mkdir(name_folder)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('img', src=re.compile('\/\/\w+\.\w+\.\w+\/...\w+..\/\w+\/\d+\.jpg'))
print(results)

print(type(results))
print(len(results))

count = 0

for result in results:
    link = result['src']
    print(link)
    img_data = requests.get(link)
    print(img_data.content)
    with open(name_folder + "/" + str(count)+".jpg", "wb") as handler:
        handler.write(img_data.content)
    count +=1