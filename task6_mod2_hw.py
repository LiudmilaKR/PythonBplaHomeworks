'''
Шаг 1.  Реализовать паттерн Итератор. Создать класс MyIterator, реализовать методы iter и next.
Шаг 2. Реализовать паттерн Наблюдатель. Создать класс MyObserver с методом update. 
Создать класс MySubject, добавить метод register для подписки, метод notify для оповещения.
Шаг 3.Реализовать паттерн Шаблонный метод. Создать абстрактный класс MyBase с шаблонным методом template_method. 
Создать классы MyClass1 и MyClass2, переопределить методы из базового класса.
Шаг 4. Протестировать Итератор, вызвав его в цикле for. 
Протестировать Наблюдатель - подписать наблюдателя, вызвать notify. 
Вызвать шаблонный метод в классах-наследниках.
'''
from abc import ABC, abstractmethod

# task 1
class Drone:
    def __init__(self, id: str, model: str, manufacturer: str) -> None:
        self._id = id
        self._model = model
        self._manufacturer = manufacturer
        
    def __iter__(self):
      return MyIterator((self._id, self._model, self._manufacturer))
    
    def __str__(self) -> str:
        return f'дрон {self._id}, {self._model}, {self._manufacturer}'
    

class MyIterator:
    def __init__(self, obj) -> None:
        self.obj = obj
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            it = self.obj[self.counter]
        except IndexError:
            raise StopIteration()
        self.counter += 1
        return it
        

# task 2
class MyObserver:
    def update(self, message: str):
        print(f'Сообщение системы: {message}')
    

class MySubject:
    def __init__(self) -> None:
        self.observers = []
    
    def register(self, observer: MyObserver):
        self.observers.append(observer)
    
    def notify(self, message: str):
        for item in self.observers:
            item.update(message)
    

# task 3
class MyBase(ABC):
    
    def __init__(self, value: int) -> None:
        self.value = value
    
    @abstractmethod
    def template_method(self):
        pass
    
    def additional_method(self, message: str):
        print(f'Сообщение: {message}')
    
    
class MyClass1(MyBase):
    def template_method(self):
        self.additional_method(f'Привет {self.value} раза')
        

class MyClass2(MyBase):
    def template_method(self):
        self.additional_method(f'До свидания {self.value} раза')


if __name__ == '__main__':
    print('Task1 - iterator')
    drone = Drone('12334A5', 'modelX', 'DroneCorp')
    print(drone)
    for el in drone:
        print(el)
    print('==========================================\n')
    
    print('Task2 - observer')
    observer1 = MyObserver()
    observer2 = MyObserver()
    observer3 = MyObserver()
    subject = MySubject()
    subject.register(observer1)
    subject.register(observer2)
    subject.register(observer3)
    subject.notify('Какое-то сообщение...')
    print('==========================================\n')
    print('Task3 - template')
    class1 = MyClass1(3)
    class1.template_method()
    class2 = MyClass2(2)
    class2.template_method()
    print('==========================================\n')
    