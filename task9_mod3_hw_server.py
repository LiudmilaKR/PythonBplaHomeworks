'''
1. Определите ресурсы для управления БПЛА, например:
    - "БПЛА" с атрибутами `id`, `name`, `status`, `location`.
    - "Миссия" с атрибутами `id`, `name`, `start_time`, `end_time`, `route`.
Шаг 2: Определение CRUD Операций

2. Реализуйте следующие CRUD операции для ресурсов "БПЛА" и "Миссия":
    - Создание нового БПЛА (HTTP метод: POST, Эндпоинт: `/drones`).
    - Получение списка всех БПЛА (HTTP метод: GET, Эндпоинт: `/drones`).
    - Получение информации о конкретном БПЛА (HTTP метод: GET, Эндпоинт: `/drones/{id}`).
    - Обновление информации о БПЛА (HTTP метод: PUT, Эндпоинт: `/drones/{id}`).
    - Удаление БПЛА (HTTP метод: DELETE, Эндпоинт: `/drones/{id}`).
    - Создание новой миссии (HTTP метод: POST, Эндпоинт: `/missions`)
    - Получение списка всех миссий (HTTP метод: GET, Эндпоинт: `/missions`).
    - Получение информации о конкретной миссии (HTTP метод: GET, Эндпоинт: `/missions/{id}`).
    - Обновление информации о миссии (HTTP метод: PUT, Эндпоинт: `/missions/{id}`).
    - Удаление миссии (HTTP метод: DELETE, Эндпоинт: `/missions/{id}`).
Шаг 3: Определение Формата Данных

3. Определите формат представления данных, например, в формате JSON.

4. Структура данных:
    - Запрос на создание/обновление БПЛА: `{"name": "Название", "status": "Статус", "location": "Местоположение"}`
    - Ответ на запрос получения списка БПЛА: `[{"id": 1, "name": "БПЛА 1", "status": "В полете", "location": "Координаты 1"}, {"id": 2, "name": "БПЛА 2", "status": "На земле", "location": "Координаты 2"}]`
    - Запрос на создание/обновление миссии: `{"name": "Название", "start_time": "Время начала", "end_time": "Время окончания", "route": "Маршрут"}`
    - Ответ на запрос получения списка миссий: `[{"id": 1, "name": "Миссия 1", "start_time": "Время начала 1", "end_time": "Время окончания 1", "route": "Маршрут 1"}, {"id": 2, "name": "Миссия 2", "start_time": "Время начала 2", "end_time": "Время окончания 2", "route": "Маршрут 2"}]`

5. Коды состояния HTTP:
    - 200 OK: Успешный запрос.
    - 201 Created: Ресурс успешно создан.
    - 404 Not Found: Ресурс не найден.
    - 400 Bad Request: Некорректный запрос.
    - 500 Internal Server Error: Внутренняя ошибка сервера.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

drones = {}
missions = {}

@app.route('/drones', methods=['POST'])
def create_drone():
    """Создание нового БПЛА"""
    drone_id = str(request.json.get('drone_id'))
    if drone_id:
        drones[drone_id] = request.json
        return jsonify({'message': f'Дрон id={drone_id} добавлен'}), 201
    return jsonify({'error': 'Не передан id дрона'}), 404

@app.route('/missions', methods=['POST'])
def create_mission():
    """Создание новой миссии"""
    mission_id = str(request.json.get('mission_id'))
    if mission_id:
        missions[mission_id] = request.json
        return jsonify({'message': f'Миссия id={mission_id} добавлена'}), 201
    return jsonify({'error': 'Не передан id миссии'}), 404

@app.route('/drones', methods=['GET'])
def get_all_drones():
    """Получение списка всех БПЛА"""
    return jsonify(drones), 200

@app.route('/missions', methods=['GET'])
def get_all_missions():
    """Получение списка всех миссий"""
    return jsonify(missions), 200

@app.route('/drones/<drone_id>', methods=['GET'])
def get_drone_by_id(drone_id):
    """Получение информации о конкретном БПЛА"""
    drone = drones.get(drone_id)
    if drone:
        return jsonify(drone), 200
    return jsonify({'error': f'Дрон id={drone_id} не найден'}), 404
    
@app.route('/drones/<drone_id>', methods=['PUT'])
def update_drone(drone_id):
    """Обновление информации о БПЛА"""
    drone = drones.get(drone_id)
    if drone:
        drones[drone_id] = request.json
        return jsonify({'message': f'Дрон id={drone_id} обновлен'}), 201
    return jsonify({'error': f'Дрон id={drone_id} не найден'}), 404

@app.route('/missions/<mission_id>', methods=['PUT'])
def update_mission(mission_id):
    """Обновление информации о миссиях"""
    mission = missions.get(mission_id)
    if mission:
        missions[mission_id] = request.json
        return jsonify({'message': f'Миссия id={mission_id} обновлена'}), 201
    return jsonify({'error': f'Миссия id={mission_id} не найден'}), 404

@app.route('/drones/<drone_id>', methods=['DELETE'])
def delete_drone(drone_id):
    """Удаление БПЛА"""
    drone = drones.get(drone_id)
    if drone:
        del drones[drone_id]
        return jsonify({'message': f'Дрон id={drone_id} удален'}), 200
    return jsonify({'error': f'Дрон id={drone_id} не найден'}), 404


if __name__ == '__main__':
    app.run(debug=True)