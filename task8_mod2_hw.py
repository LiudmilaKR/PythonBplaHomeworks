'''
Шаг 1. Создать интерфейс класса SomeObject с методами, предоставляющими доступ к данным.
Шаг 2. Реализовать класс Proxy, который реализует интерфейс SomeObject. 
В его методах добавить проверку прав доступа перед вызовом методов реального объекта.
Шаг 3. Реализовать класс SecureProxy. Также реализовать интерфейс SomeObject. 
В его методах добавить дополнительные проверки безопасности.
'''

import jwt
import task8_mod2_hw_server
import time

SECRET_KEY = 'myKEY12345'

class SomeObject:
    def __init__(self, id: int, name: str) -> None:
        self._id = id
        self._name = name
    
    def action1(self):
        print(f'Action1 for id={self._id}, name={self._name}')
        
    def action2(self):
        print(f'Action2 for id={self._id}, name={self._name}')
        

class ProxyObject:
    def __init__(self, obj: SomeObject) -> None:
        self._obj = obj
        
    def action1(self):
        print('Реализация метода action1')
        self._obj.action1()
        
    def action2(self):
        print('Реализация метода action2')
        self._obj.action2()
        

class SecureProxyObject:
    def __init__(self, obj: SomeObject, token) -> None:
        self._obj = obj
        self._token = token
    
    def verify_token(self):
        try:
            payload = jwt.decode(self._token, SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            print('Токен истек')
            return None
        except jwt.InvalidTokenError:
            print('Токен не валиден')
            return None
    
    def action1(self):
        if self.verify_token():
            print('Реализация метода action1')
            self._obj.action1()
        else:
            print('Доступ запрещён: ошибка авторизации')
        
    def action2(self):
        if self.verify_token():
            print('Реализация метода action2')
            self._obj.action2()
        else:
            print('Доступ запрещён: ошибка авторизации')
            

def request_token(user_id):
    return task8_mod2_hw_server.generate_token(user_id)


if __name__ == '__main__':
    some_obj = SomeObject(25, 'idea')
    print('Реализация класса ProxyObject')
    obj_proxy = ProxyObject(some_obj)
    obj_proxy.action1()
    obj_proxy.action2()
    print('===================================')
    print()
    print('Реализация класса SecureProxyObject')
    user_id = 'Inga'
    token = request_token(user_id)
    print(f'{user_id} получил токен:\n{token}')
    obj_secure_proxy = SecureProxyObject(some_obj, token)
    obj_secure_proxy.action1()
    time.sleep(8)
    obj_secure_proxy.action2()
