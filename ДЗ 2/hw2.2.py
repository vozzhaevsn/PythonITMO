#Создаем список кортежей имя плюс возраст
list_tuple = [('Ruby', 15), ('Bob', 10), ('Misha', 34), ('Semyon', 26)]

#создаем список с условием сортировки по элементу возраста в кортежах
list_tuple2 = sorted(l for l in list_tuple if l[1]> 18)

#Выводим результат
print(list_tuple2)