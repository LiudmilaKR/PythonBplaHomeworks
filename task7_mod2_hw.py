'''
Шаг 1. Реализовать паттерн Абстрактная фабрика для работы с БД. 
Создать интерфейс базового класса DBFactory и классы MySQLFactory, PostgreSQLFactory и др.
Шаг 2. Реализовать паттерн Строитель для создания запросов. 
Создать класс QueryBuilder с методами select(), where(), order_by() и др.
Шаг 3. Реализовать Отображение объектно-реляционное. Создать класс User, класс UserMapper для 
преобразования User в строку SQL и обратно.
Шаг 4. Реализовать паттерн Хранитель для управления соединениями с БД. 
Класс DBConnectionManager будет отвечать за установку, разрыв соединений.
Шаг 4. Протестировать реализованные паттерны. Создать подключения через фабрику. 
Построить запрос со строителем. Получить данные, преобразовать их в объекты с отображением ОР.
'''

from abc import ABC, abstractmethod
import sqlite3
# import MySQLdb
import mysql.connector
import psycopg2


class BDFactory(ABC):
    @abstractmethod
    def connect(self):
        pass


class SQLiteFactory(BDFactory):
    def connect(self):
        return sqlite3.connect('test.db') 


class MySQLFactory(BDFactory):
    def connect(self):
        return mysql.connector.connect(host='127.0.0.1', user='newuser', passwd='***', database='bpla')
        # return MySQLdb.connect('127.0.0.1', 'newuser', '***', 'bpla')

class PostgresSQLFactory(BDFactory):
    def connect(self):
        return psycopg2.connect(database='postgres', user='postgres', password='***', host='localhost')


class QueryBuilder():
    def __init__(self) -> None:
        self._query = {
            'select': None,
            'where': None,
            'order_by': None,
            'insert_into': None
        }
        self._params = []
        
        
    def select(self, table, columns='*'):
        self._query['select'] = f'SELECT {columns} FROM {table}'
        return self
    
    
    def where(self, condition):
        self._query['where'] = f'WHERE {condition}'
        return self
    
    
    def order_by(self, order, ord='ASC'):
        self._query['order_by'] = f'ORDER BY {order} {ord}'
        return self
    
    
    def get_query(self):
        if self._query['select']:
            query = f'{self._query["select"]}'
        if self._query['where']:
            query += f'\n{self._query["where"]}'
        if self._query['order_by']:
            query += f'\n{self._query["order_by"]}'
        print(query)
        return query


class User:
    def __init__(self, id, name, contact) -> None:
        self.id = id
        self.name = name
        self.contact = contact
        
    def __str__(self) -> str:
        return f'Operator id={self.id}, name={self.name}'
        
    
class UserMapper:
    def __init__(self, connection) -> None:
        self.connection = connection

    
    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tbl_operators')
        result = cursor.fetchall()
        return result
    
    def get_user(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT * FROM tbl_operators WHERE id={id}')
        result = cursor.fetchone()
        if result:
            return User(id=result[0], name_operator=result[1], contact=result[2])
        return None
    
    def add_user(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO tbl_operators(name_operator, contact) VALUES(?, ?)', 
                       (user.name, user.contact))


class DBConnectionManager():
    def __init__(self, bd: BDFactory) -> None:
        self._bd = bd
        self._connection = None
        
    def get_connection(self):
        """Подключение к базе данных"""
        if self._connection is None:
            self._connection = self._bd.connect()
        return self._connection
    
    def close_connection(self):
        """закрытие подключения к базе данных"""
        if self._connection:
            self._connection.close()
            self._connection = None

    
if __name__ == '__main__':
    sqlite_bd = SQLiteFactory()
    connection_management = DBConnectionManager(sqlite_bd)
    connection = connection_management.get_connection()
    
    cursor = connection.cursor()
    query_builder = QueryBuilder()
    query = query_builder.select('tbl_drones', 'id, serial_number') \
            .where('(id = 2 OR id = 3)').order_by('id', 'DESC').get_query()
    cursor.execute(query)
    res = cursor.fetchall()
    print('========================================================')
    print('Выводим результат запроса в базу данных sqlite:')
    for el in res:
        print(el)
    
    operator = UserMapper(connection)
    operator.add_user(User('2', 'Anna', 'operator1@testmail.com'))
    operator.add_user(User('3', 'Petr', 'operator2@testmail.com'))
    operators = operator.get_all_users()
    print('--------------------------------------------------------')
    print('Выводим операторов:')
    for item in operators:
        print(item)
    connection_management.close_connection()
    print()
    
    mysql_bd = MySQLFactory()
    connection_management = DBConnectionManager(mysql_bd)
    connection = connection_management.get_connection()
    
    cursor = connection.cursor()
    query_builder = QueryBuilder()
    query = query_builder.select('tbl_drones') \
            .where('(id = 7 OR id = 8 OR id = 9)').order_by('id', 'DESC').get_query()
    cursor.execute(query)
    res = cursor.fetchall()
    print('========================================================')
    print('Выводим результат запроса в базу данных mysql:')
    for el in res:
        print(el)
    connection_management.close_connection()
    print()
    
    postgres_bd = PostgresSQLFactory()
    connection_management = DBConnectionManager(postgres_bd)
    connection = connection_management.get_connection()
    # connection.autocommit = True
    
    cursor = connection.cursor()
    query_builder = QueryBuilder()
    query = query_builder.select('tbl_drones') \
            .where('(id = 3 OR id = 4 OR id = 5)').order_by('id', 'DESC').get_query()
    cursor.execute(query)
    res = cursor.fetchall()
    print('========================================================')
    print('Выводим результат запроса в базу данных postgres:')
    for el in res:
        print(el)
    connection_management.close_connection()
    