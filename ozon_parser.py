import re #отвечает за регулярные выражения
import requests #библиотека, которая у нас отвечает за веб запросы
from bs4 import BeautifulSoup #просто парсер
import os #Для создания папок


URL = input("Введите URL, который вы хотите спарсить: \n")
name_folder = input("Введите название папки: \n")
os.mkdir(name_folder)
page = requests.get(URL.strip())

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