import requests

BASE_URL = 'http://127.0.0.1:5000/drones'
BASE_URL1 = 'http://127.0.0.1:5000/missions'


def add_drone(drone_id, drone_info):
    url = BASE_URL
    payload = {
        'drone_id': drone_id,
        **drone_info
    }
    response = requests.post(url, json=payload)
    return response.json()

def add_mission(mission_id, mission_info):
    url = BASE_URL1
    payload = {
        'mission_id': mission_id,
        **mission_info
    }
    response = requests.post(url, json=payload)
    return response.json()

def get_all_drones():
    url = BASE_URL
    response = requests.get(url)
    return response.json()

def get_all_missions():
    url = BASE_URL1
    response = requests.get(url)
    return response.json()

def get_drone_by_id(drone_id):
    url = f'{BASE_URL}/{drone_id}'
    response = requests.get(url)
    return response.json()

def update_drone(drone_id, drone_info):
    url = f'{BASE_URL}/{drone_id}'
    payload = {
        'drone_id': drone_id,
        **drone_info
    }
    response = requests.put(url, json=payload)
    return response.json()

def update_mission(mission_id, mission_info):
    url = f'{BASE_URL1}/{mission_id}'
    payload = {
        'mission_id': mission_id,
        **mission_info
    }
    response = requests.put(url, json=payload)
    return response.json()

if __name__ == '__main__':
    drone_id_1 = 1
    drone_info_1 = {
        'name': 'БПЛА 1',
        'status': 'В полете',
        'location': 'Координаты 1'
    }
    drone_id_2 = 2
    drone_info_2 = {
        'name': 'БПЛА 2',
        'status': 'На земле',
        'location': 'Координаты 2'
    }
    response1 = add_drone(drone_id_1, drone_info_1)
    response2 = add_drone(drone_id_2, drone_info_1)
    print(response1)
    print(response2)
    print('\nСписок всех дронов:')
    print(get_all_drones())
    print(f'\nДрон с id={drone_id_1}: {get_drone_by_id(drone_id_1)}')
    print(f'\nОбновление дрона id={drone_id_1}')
    drone_info_3 = {
        'name': 'БПЛА 11',
        'status': 'На земле',
        'location': 'Координаты 11'
    }
    response3 = update_drone(drone_id_1, drone_info_3)
    print(response3)
    print('\n======================================================')
    mission_id_1 = 1
    mission_info_1 = {
        'name': 'Миссия 1',
        'start_time': 'Время начала 1',
        'end_time': 'Время окончания 1',
        'route': 'Маршрут 1'
    }
    mission_id_2 = 2
    mission_info_2 = {
        'name': 'Миссия 2',
        'start_time': 'Время начала 2',
        'end_time': 'Время окончания 2',
        'route': 'Маршрут 2'
    }
    response4 = add_mission(mission_id_1, mission_info_1)
    response5 = add_mission(mission_id_2, mission_info_1)
    print(response4)
    print(response5)
    print('\nСписок всех миссий:')
    print(get_all_missions())
    print(f'\nОбновление миссии id={mission_id_1}')
    mission_info_3 = {
        'name': 'Миссия 11',
        'start_time': 'Время начала 21',
        'end_time': 'Время окончания 21',
        'route': 'Маршрут 22'
    }
    response6 = update_mission(mission_id_1, mission_info_3)
    print(response6)
