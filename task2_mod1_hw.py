"""
В рамках задания вам необходимо примененить ООП в контексте разработки для БПЛА.

Инструкция:
Шаг 1. Создать классы Drone (беспилотник), Camera (камера), GPS (система GPS) и FlightController (контроллер полета).
Шаг 2. Добавить в класс Drone поля для объектов Camera, GPS и FlightController. 
Таким образом беспилотник будет содержать эти компоненты.
Шаг 3. Добавить в класс FlightController методы для управления полетом беспилотника - взлет, посадка, изменение высоты и координат. 
Вызывать эти методы для объекта класса Drone.    
"""
import random


class Drone:
    
    def __init__(self, id='123F56', altitude=0, coords=(0.0, 0.0)) -> None:
        self.id = id
        self.altitude = altitude
        self.coordinates = coords
        self.camera = Camera()
        self.gps = GPS()
        self.flight_controller = FlightController()
        self.flight_path = []
        self.ar_altitudes = []
        print('Создан экземпляр класса Drone')
    
    def drone_runways(self, rise_altitude):
        """_summary_ метод взлета БПЛА

        Args:
            altitude (_type_): _description_ высота взлета БПЛА

        Returns:
            _type_: _description_ высота взлета
        """
        self.altitude = self.flight_controller.runways(rise_altitude)
        self.ar_altitudes.append(self.altitude)
        print(f'БПЛА взлетает на высоту {self.altitude} метров')
    
    def change_altitude(self, new_altitude: int):
        """_summary_ метод изменения высоты БПЛА

        Args:
            altitude (int): _description_ новая высота
        """
        if self.altitude > new_altitude:
            print(f'БПЛА снижается на {new_altitude} метров')
        else:
            print(f'БПЛА меняет высоту на {new_altitude} метров')
        self.altitude = self.flight_controller.change_altitude(new_altitude)
        self.ar_altitudes.append(self.altitude)
    
    def change_coords(self, new_coords: tuple):
        """_summary_ метод изменения координат БПЛА

        Args:
            new_coords (tuple): _description_ новые координаты БПЛА
        """
        self.coordinates = self.gps.update_coord(new_coords)
        self.flight_path.append(self.coordinates)
        print(f'Новые координаты БЛПА {self.coordinates}')
    
    def drone_landing(self):
        """_summary_ метод посадки БПЛА

        """
        print(self.flight_controller.landing())
        print(f'Отчет о полёте БПЛА id={self.id}:\nКоординаты полёта {self.flight_path}\nВысоты {self.ar_altitudes}')
    
    def __str__(self) -> str:
        return f'БПЛА {self.id} с камерой: {self.camera}, начальные координаты {self.gps.coordinates}'

class Camera:
    
    def __init__(self, model='CD06', resolution='640x510') -> None:
        self.model = model
        self.resolution = resolution
        # print('Создан экземпляр класса Camera')
        
    def __str__(self) -> str:
        return f'модель {self.model} разрешение {self.resolution} пикселей'


class GPS:
    
    def __init__(self, init_coords = (0.0, 0.0)) -> None:
        self.coordinates = init_coords
        # print('Создан экземпляр класса GPS')
    
    def update_coord(self, coords: tuple):
        self.coordinates = coords
        return self.coordinates

class FlightController:
        
    def runways(self, rise_altitude: int):
        if rise_altitude > 0:
            return rise_altitude
        else:
            raise ValueError('Высота взлета должна быть > 0')
        
    def landing(self):
        return 'БПЛА приземлился'
        
    def change_altitude(self, new_altitude: int):
        if new_altitude > 0:
            return new_altitude
        else:
            raise ValueError('Высота взлета должна быть > 0')


if __name__ == '__main__':
    drone1 = Drone()
    print(drone1.__str__())
    drone1.drone_runways(15)
    new_coords = round(random.uniform(-50.0, 50.0), 4), round(random.uniform(-50.0, 50.0), 4)
    drone1.change_coords(new_coords)
    drone1.change_altitude(25)
    new_coords = round(random.uniform(-50.0, 50.0), 4), round(random.uniform(-50.0, 50.0), 4)
    drone1.change_coords(new_coords)
    drone1.change_altitude(12)
    new_coords = round(random.uniform(-50.0, 50.0), 4), round(random.uniform(-50.0, 50.0), 4)
    drone1.change_coords(new_coords)
    drone1.drone_landing()