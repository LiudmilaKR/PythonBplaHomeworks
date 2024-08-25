'''
Шаг 1. Реализовать аутентификацию пользователей с помощью JWT токенов.
Шаг 2. Добавить проверки входных данных на валидность перед отправкой команд беспилотнику.
Шаг 3. Автоматизация парсинга нескольких страниц
Шаг 4. Обрабатывать возможные ошибки при работе с беспилотником и корректно отвечать клиенту с описанием проблемы.
'''

from flask import Flask, Response, request, jsonify
import logging
from flask_jwt_extended import (JWTManager, create_access_token, 
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
my_jwt = JWTManager(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
    """Регистрация нового пользователя.

    Returns:
        JSON-ответ с сообщением об успешной регистрации и статус-код 201,
        или ошибка 400, если пользователь уже существует
    """
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users:
        return jsonify({'error': 'Пользователь с таким именем уже существует'}), 400
    users[username] = password
    return jsonify({'message': f'Пользователь {username} добавлен'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Авторизация пользователя и получение JWT-токена.

    Returns:
        JSON-ответ с токеном и статус-код 200,
        или ошибка 403, если логин или пароль неверны
    """
    username = request.json.get('username')
    password = request.json.get('password')
    if users[username] != password:
        return jsonify({'error': 'Неверный пользователь или пароль'}), 403
    token = create_access_token(identity=username)
    return jsonify(token=token), 200

@app.route('/takeoff/<drone_id>', methods=['POST'])
@jwt_required()
def takeoff(drone_id):
    """Обрабатываем запрос на взлет дрона.

    Return: JSON-ответ с сообщением о результате взлета
    """
    altitude = request.json.get('altitude')
    if altitude:
        return jsonify({'message': f'Дрон id={drone_id} взлет на высоту {altitude} метров выполнил'}), 200
    else:
        return jsonify({'message': 'Данные по высоте не переданы'}), 204


if __name__ == '__main__':
    app.run(debug=True)
