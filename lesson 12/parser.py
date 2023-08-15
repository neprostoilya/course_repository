import requests
import unicodedata
from bs4 import BeautifulSoup as BS4
import json

while True:
    URL = input('Введите ссылку: ')
    if not URL: break 

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36'}
    html = requests.get(URL, headers=HEADERS).text
    soup = BS4(html, 'html.parser')
    json_data = []
    for i in ['w_col_wide2', 'w_col1', 'w_col2', 'w_col_wide']:
        for article in soup.find_all('div', class_=i):
            for title in article.find_all('div', class_='b_ear-title'): title = title.get_text(strip=True)
            for intro in article.find_all('div', class_='b_ear-intro'): intro = intro.get_text(strip=True)
            for time in article.find_all('time', class_='b_ear-time'): time = time.get_text(strip=True)
            for image in article.find_all('img'): image = image['src']
            
            json_data.append({
            'title': unicodedata.normalize('NFKD',title),
            'context': unicodedata.normalize('NFKD', intro),
            'publication': unicodedata.normalize('NFKD', time),
            'image_link': image
        })
        with open(f'gazeta_ru.json', mode='w', encoding='UTF-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)