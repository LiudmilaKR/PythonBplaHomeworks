'''
Шаг 1. Разработать сервер на Node.js, который будет возвращать текущую дату и время в формате JSON по запросу GET /time.
Шаг 2. Разработать клиент на Python с использованием библиотеки Requests, который будет делать запрос к 
разработанному серверу и выводить полученный ответ.
Шаг 3. Запустить сервер и клиент, протестировать работу. Убедиться, что клиент корректно получает данные от сервера.
'''

import requests

BASE_URL = 'http://localhost:3001'

def send_command(command):
    try:
        response = requests.get(f'{BASE_URL}/{command}')
        if response.status_code == 200:
            data = response.json()
            print(f'Текущая дата: {data}')
        else:
            print(f'Ошибка данных: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка запроса: {e}')


if __name__ == '__main__':
    send_command('time')
