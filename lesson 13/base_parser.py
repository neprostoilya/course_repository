import requests
from configs import *
import json


class BaseParser:
    def __init__(self):
        self.url = URL
        self.host = HOST

    def get_html(self, link):
        return requests.get(link).text

    @staticmethod
    def save_data_to_json(path, data):
        with open(f'{path}.json', mode='w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


