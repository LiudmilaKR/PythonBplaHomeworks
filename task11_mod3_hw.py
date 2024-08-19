'''
Шаг 1. Разработать сервер на Node.js, который будет выступать как оберточный API.
Шаг 2. Реализовать авторизацию и аутентификацию пользователей.
Шаг 3. Реализовать endpoint'ы оберточного API для управления беспилотником, 
обрабатывающие запросы и передающие данные в API беспилотника.
'''

from abc import ABC, abstractmethod
import requests

class IControlDrone(ABC):
    @abstractmethod
    def __init__(self, base_url):
        pass
    
    @abstractmethod
    def takeoff(self, drone_id):
        pass
    
    @abstractmethod
    def land(self, drone_id):
        pass


class ControlDroneNodejs(IControlDrone):
    def __init__(self, base_url):
        self.base_url = base_url
        
    def takeoff(self, drone_id):
        try:
            response = requests.get(f'{self.base_url}/{drone_id}/takeoff')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Ошибка взлета: {e}')
            
    def land(self, drone_id):
        try:
            response = requests.get(f'{self.base_url}/{drone_id}/land')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Ошибка взлета: {e}')
            
if __name__ == '__main__':
    BASE_URL = 'http://localhost:3001'
    node_js = ControlDroneNodejs(BASE_URL)
    print(node_js.takeoff(drone_id='1'))
    print(node_js.takeoff(drone_id='2'))
    print(node_js.land(drone_id='1'))
    print(node_js.land(drone_id='2'))
