0#Создаем список чисел
list_start = int(input('Введите начало списка:'))
list_end = int(input('Введите конец списка:'))
list_1 = list(range(list_start, list_end))
#Выводим список чисел
print('Ваш список:', list_1)
#Новый список с возведенными в куб числами
cub_list = list(map(lambda x: x ** 3, list_1))
print(cub_list)
#Отбор четных элементов
filter_list = list(filter(lambda x: x % 2 == 0, cub_list))
print(filter_list)
#произведение получившихся значений
from functools import reduce
reduce_list = reduce(lambda x, y: x * y, filter_list)
print(reduce_list)