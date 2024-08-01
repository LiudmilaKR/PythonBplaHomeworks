'''
В рамках задания вам необходимо сделать работу с Singleton, Adapter, Decorator.
Инструкция:
Шаг 1. Создать класс MySingleton. Добавить в него статическое поле instance и 
метод get_instance для получения единственного экземпляра класса.
Шаг 2. В методе init класса MySingleton проверить, существует ли уже экземпляр в instance. 
Если нет - создать новый и сохранить в instance.
Шаг 3.Вызвать метод get_instance дважды в коде и убедиться, что он возвращает один и тот же экземпляр класса.
Шаг 4. Создать класс MyClass с методом test. Создать класс MyClassAdapter, в нем вызвать метод test из экземпляра MyClass.
Шаг 5. Создать функцию my_function. Написать декоратор my_decorator, который будет выводить имя функции перед ее вызовом.
Шаг 6. Применить декоратор к функции my_function и убедиться, что при вызове функции выводится ее имя.
'''

class MySingleton:
    
    __instance = None
    
    def __init__(self, name: str) -> None:
        if MySingleton.__instance == None:
            MySingleton.__instance = name
            print(f'Создали экземляр класса MySingleton {name}')
        else:
            print('Экземляр класса MySingleton уже существует!')
    
    @classmethod
    def get_instance(cls):
        return cls.__instance

# Решение преподавателя
class MySingleton1:
    __instance = None

    def __init__(self):
        if MySingleton1.__instance is not None:
            print('Ветка init: MySingleton1 is not None')
            raise Exception('Этот класс является синглтоном!')
        else:
            print('Ветка init: MySingleton1.__instance = self')
            MySingleton1.__instance = self

    @staticmethod
    def get_instance():
        if MySingleton1.__instance is None:
            print('Создаем экземпляр синглетона')
            MySingleton1()
        return MySingleton1.__instance
    
    # def __repr__(self) -> str:
    #     return str(self.__instance)
    

class MyClass:
    def test(self):
        print(f'Работа метода test из класса MyClass')    
        
        
class MyClassAdapter():
    def __init__(self, my_class: MyClass) -> None:
        self.my_class = my_class
        
    def test_adapter(self):
        print('Результат работы метода test_adapter из класса MyClassAdapter является => ')
        return self.my_class.test()
  

def my_decorator(func):
    def wrapper():
        print('Action before')
        func()
        print('Action after')
    return wrapper


@my_decorator    
def my_function():
    print('Функция my_function')


if __name__ == '__main__':
    print('Задание по Singleton')
    singleton1 = MySingleton('singleton1')
    print(singleton1.get_instance())
    singleton2 = MySingleton('singleton2')
    print(singleton2.get_instance())
    print(MySingleton.get_instance())
    print('================================')
    print()
    
    # Проверка Singleton1
    print('Задание по Singleton1')
    singleton3 = MySingleton1()
    print(f'singleton3 = {singleton3.__repr__()}')
    singleton1 = MySingleton1.get_instance()
    singleton2 = MySingleton1.get_instance()
    print('================================')
    print()

    print('Задание по Adapter')
    my_adapter = MyClassAdapter(MyClass())
    my_adapter.test_adapter()
    print('================================')
    print()

    print('Задание по Decorator')
    my_function()

