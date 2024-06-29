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
        """_summary_ Конструктор объекта класса Drone

        Args:
            id (str, optional): _description_. Defaults to '123F56'. id объекта класса Drone
            altitude (int, optional): _description_. Defaults to 0. высота полёта объекта класса Drone
            coords (tuple, optional): _description_. Defaults to (0.0, 0.0). координаты объекта класса Drone
        """
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
        """_summary_ метод взлета объекта класса Drone

        Args:
            altitude (_type_): _description_ высота взлета объекта класса Drone
        """
        self.altitude = self.flight_controller.runways(rise_altitude)
        self.ar_altitudes.append(self.altitude)
        print(f'БПЛА взлетает на высоту {self.altitude} метров')
    
    def change_altitude(self, new_altitude: int):
        """_summary_ метод изменения высоты объекта класса Drone

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
        """_summary_ метод изменения координат объекта класса Drone

        Args:
            new_coords (tuple): _description_ новые координаты объекта класса Drone
        """
        self.coordinates = self.gps.update_coord(new_coords)
        self.flight_path.append(self.coordinates)
        print(f'Новые координаты БЛПА {self.coordinates}')
    
    def drone_landing(self):
        """_summary_ метод посадки объекта класса Drone

        """
        print(self.flight_controller.landing())
        print(f'Отчет о полёте БПЛА id={self.id}:\nКоординаты полёта {self.flight_path}\nВысоты {self.ar_altitudes}')
    
    def __str__(self) -> str:
        """_summary_ метод отображения информации об объекте клаcса Drone

        Returns:
            str: _description_ информация об объекте класса Drone
        """
        return f'БПЛА {self.id} с камерой: {self.camera}, начальные координаты {self.gps.coordinates}'
    

class Camera:
    
    def __init__(self, model='CD06', resolution='640x510') -> None:
        """_summary_ конструктор объекта класса Camera

        Args:
            model (str, optional): _description_. Defaults to 'CD06'. модель объекта класса Camera
            resolution (str, optional): _description_. Defaults to '640x510'. разрешение объекта класса Camera
        """
        self.model = model
        self.resolution = resolution
        
    def __str__(self) -> str:
        """_summary_ метод отображения информации об объекте клаcса Camera

        Returns:
            str: _description_ информация об объекте класса Camera
        """
        return f'модель {self.model} разрешение {self.resolution} пикселей'


class GPS:
    
    def __init__(self, init_coords = (0.0, 0.0)) -> None:
        """_summary_ конструктор объекта класса GPS

        Args:
            init_coords (tuple, optional): _description_. Defaults to (0.0, 0.0). начальные координаты
        """
        self.coordinates = init_coords
    
    def update_coord(self, coords: tuple):
        """_summary_ метод обновления координат

        Args:
            coords (tuple): _description_ координаты

        Returns:
            _type_: _description_ кортеж координат
        """
        self.coordinates = coords
        return self.coordinates

class FlightController:
        
    def runways(self, rise_altitude: int):
        """_summary_ метод управления взлетом

        Args:
            rise_altitude (int): _description_ высота взлета

        Raises:
            ValueError: _description_ 

        Returns:
            _type_: _description_ высота взлета
        """
        if rise_altitude > 0:
            return rise_altitude
        else:
            raise ValueError('Высота взлета должна быть > 0')
        
    def landing(self):
        """_summary_ метод управления приземлением

        Returns:
            _type_: _description_ сооббщение о приземлении
        """
        return 'БПЛА приземлился'
        
    def change_altitude(self, new_altitude: int):
        """_summary_ метод изменения высоты полёта

        Args:
            new_altitude (int): _description_ новая высота полёта

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_ высота полета
        """
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