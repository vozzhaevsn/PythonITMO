#Вызываем библиотеку requests
import requests

# Указываем имя пользователя GitHub
username = 'D-Zaharov'  
# Формируем URL-адрес, подставляя значение username
url = f'https://api.github.com/users/{username}'
response = requests.get(url)
# Проверяем, был ли запрос успешным (статус-код 200). Если да, то извлекаем необходимые данные
if response.status_code == 200:
    data = response.json()
    print(f"Имя пользователя: {data['name']}")
    print(f"Логин: {data['login']}")
    print(f"Количество репозиториев: {data['public_repos']}")
else:
    print(f"Ошибка при получении данных: {response.status_code}")
