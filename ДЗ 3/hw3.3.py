#Создаем основную функцию для работы со списком
def own_map(func, my_list):
    result = []
    for i in my_list:
        result.append(func(i))
    return result

#Функция умножения значений на само себя
def square(x):
    return x * x

#Создаем список
list_start = int(input('Введите начало списка:'))
list_end = int(input('Введите конец списка:'))
list_1 = list(range(list_start, list_end))
print('Ваш список:', list_1)

#Выводим результат
squared_numbers = own_map(square, list_1)
print(squared_numbers)