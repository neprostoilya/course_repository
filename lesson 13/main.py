from configs import *
from base_parser import BaseParser
import time

from bs4 import BeautifulSoup 

class CategoryParser(BaseParser):
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATA = {}

    def category_block_parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for category in soup.find_all('a', class_='css-rc5s2u'):    
            category_title = category.find(class_='css-u2ayx9').find('h6').get_text(strip=True)
            category_link = self.host + category.get('href')
            
            category_price = category.find(class_='css-u2ayx9').find('p').get_text(strip=True)
            category_page = self.get_html(category_link)
            self.DATA[category_title] = []
            self.category_page_parser(category_page, category_title, category_price, category_link)

    def category_page_parser(self, category_page, category_title, category_price, category_link):
        soup =  BeautifulSoup(category_page, 'html.parser')
        category_1 = soup.find_all('div', class_='css-n9feq4')
        for category in category_1:
            category_time = category.find(class_='css-19yf5ek').get_text(strip=True)
            category_description = category.find(class_='css-bgzo2k er34gjf0').get_text(strip=True)
            print(category_time)
            print(category_title)
            print(category_description)
            print(category_price)
            print(category_link)
            self.DATA[category_title].append({
                "Дата публикации": category_time,
                "Имя продукта": category_title,
                "Описание": category_description,
                "Цена продукта": category_price,
                "Ссылка на товар": category_link,
            })
           
        time.sleep(4)


def start_category_parsing():
    parser = CategoryParser()
    # category= input('Введите  категорию: ')
    category_1 = input('Введите главную категорию: ')
    category_2 = input('Введите под категорию: ')
    category_link = 'https://www.olx.uz/d/oz/'   + category_1 + '/' + category_2 + '/'
    print(Color.RED + 'Парсер начал работу')
    start = time.time()
    html = parser.get_html(category_link)
    parser.category_block_parser(html)
    parser.save_data_to_json(category_2, parser.DATA)
    finish = time.time()
    print(Color.WHITE + f'Парсер завершил работу за {round(finish - start, 2)} секунд')


start_category_parsing()