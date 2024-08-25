import requests
import logging
from bs4 import BeautifulSoup
import urllib.parse
import re
import json

BASE_URL = 'http://127.0.0.1:5000'

def register(username, password):
    url = f'{BASE_URL}/register'
    response = requests.post(url, json={'username':username, 'password': password})
    if response.status_code == 201:
        logging.info(f'Пользователь {username} зарегистрирован')
    elif response.status_code == 400:
        logging.info(f'Пользователь {username} уже зарегистрирован')

def login(username, password):
    url = f'{BASE_URL}/login'
    response = requests.post(url, json={'username':username, 'password': password})
    if response.status_code == 200:
        logging.info(f'Пользователь {username} авторизирован')
        return response.json().get('token')
    elif response.status_code == 403:
        logging.info(f'Пользователь {username} не авторизирован')

def takeoff(drone_id, altitude, token):
    url = f'{BASE_URL}/takeoff/{drone_id}'
    payload = {'drone_id': drone_id, 'altitude': altitude}
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get('message')

def parsing_some_pages(page_url, file_path):
    cur_page_url = page_url
    common_list = []
    while True:
        response = requests.get(cur_page_url, headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})
        soup = BeautifulSoup(response.content, 'html.parser')
        for item in soup.find_all('article', class_='product_pod'):
            item_dict = {}
            
            item_name = item.find('h3').find('a')
            item_dict['title'] = item_name.get('title') if item_name else 'None'
            item_url = item_name.get('href') if item_name else ''
            
            item_price = item.find('div', class_='product_price').find('p', class_='price_color')
            item_dict['price'] = item_price.text if item_price else 'None'

            if item_url != '':
                item_full_url = urllib.parse.urljoin(cur_page_url, item_url)
            
            if item_full_url:
                resp_item = requests.get(item_full_url)
                soup_item = BeautifulSoup(resp_item.content, 'html.parser')
                item_q = soup_item.find('p', class_='instock availability')
                item_q = item_q.text.strip() if item_q else 0
                item_q = int(re.sub('[^0-9]', '', item_q))
                item_dict['qauntity'] = item_q
                
                item_d = soup_item.find('div', class_='sub-header').findNext('p')
                item_d = item_d.text if item_d else 'None'
                item_dict['description'] = item_d
            common_list.append(item_dict)
    
        next_page = soup.find('li', ('class', 'next'))
        num = 0
        if next_page:
            if num < 5:
                next_page_url = next_page.find('a').get('href')
                # print('next_page_url=', next_page_url)
                num = int(next_page_url.split('-')[1].split('.')[0])
                cur_page_url = urllib.parse.urljoin(cur_page_url, next_page_url)
            else:
                break
        else:
            break
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(common_list, f, indent=2)

if __name__ == '__main__':
    print('Реализация аутентификации пользователей с помощью JWT токенов.')
    username = 'Liza'
    password = '123'
    
    register(username, password)
    token = login(username, password)
    drone_id = 555
    print()
    print('===========================================================================================')
    print('Проверка входных данных на валидность перед отправкой команд беспилотнику.')
    if token:
        print('Выполнение takeoff:')
        altitude = 200
        response = takeoff(drone_id, altitude, token)
        print(response)
    else:
        print('Авторизация не прошла')
    print()
    print('===========================================================================================')
    print('Автоматизация парсинга нескольких страниц')
    parsing_some_pages('http://books.toscrape.com/', 'books.json')
    