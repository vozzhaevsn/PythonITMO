# Импортируем модули string и random
import string
import random

def generate_password(length):
    # Определяем набор символов для пароля
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем случайный пароль
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Запрашиваем длину пароля
password_length = int(input("Введите длину пароля: "))

# Генерируем пароль
password = generate_password(password_length)
print("Сгенерированный пароль:", password)
