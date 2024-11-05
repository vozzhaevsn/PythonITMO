from flask import Flask, request, jsonify  # Импортируем необходимые модули
from hashtable import HashTable  # Импортируем реализацию хэш таблицы

app = Flask(__name__)  # Создаем экземпляр сервера Flask
hash_table = HashTable()  # Создаем экземпляр хэш таблицы

@app.route('/add', methods=['GET'])  # Создание обработчика GET-запросов по адресу "/add"
def add():
    a = request.args.get('a', type=int)  # Получение значения параметра "a" из GET-запроса
    b = request.args.get('b', type=int)  # Получение значения параметра "b" из GET-запроса
    result = a + b  # Выполнение операции сложения
    return jsonify({  # Формирование ответа в JSON-формате
        'operation': 'addition',
        'parameters': {'a': a, 'b': b},
        'result': result
    })

@app.route('/hash_insert', methods=['POST'])  # Создание обработчика POST-запросов по адресу "/hash_insert"
def hash_insert():
    data = request.get_json()  # Получение данных из тела POST-запроса в формате JSON
    key = data.get('key')  # Извлечение ключа из полученных данных
    value = data.get('value')  # Извлечение значения из полученных данных
    hash_table.insert(key, value)  # Вставка значения в хэш таблицу
    return jsonify({'status': 'success', 'message': f'Inserted {key}: {value}'})  # Формирование ответа в JSON-формате

@app.route('/hash_get', methods=['GET'])  # Создание обработчика GET-запросов по адресу "/hash_get"
def hash_get():
    key = request.args.get('key')  # Получение значения параметра "key" из GET-запроса
    value = hash_table.get(key)  # Получение значения из хэш таблицы по ключу
    if value is not None:
        return jsonify({'key': key, 'value': value})  # Формирование ответа в JSON-формате
    else:
        return jsonify({'error': 'Key not found'}), 404  # Формирование ответа об ошибке в JSON-формате с кодом 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Запуск сервера на локальной машине по адресу http://0.0.0.0:5000/

#Пример инструкции по приминению
# - Для выполнения операции сложения: отправьте GET-запрос на http://localhost:5000/add?a=5&b=10.
# - Для вставки в хэш таблицу: отправьте POST-запрос на http://localhost:5000/hash_insert с JSON телом {"key": "a", "value": 1}.
# - Для получения значения: отправьте GET-запрос на http://localhost:5000/hash_get?key=a