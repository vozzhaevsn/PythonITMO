my_list = []

while True:
    try:
        my_input = int(input('Введите любое целое число и нажимите "Enter". Чтобы закончить ввод данных, наберите "-1": '))
        if my_input == -1:
            print('Ввод закончен.')
            break
        my_list.append(my_input)
        
    except ValueError:
        print('Ошибка! Введите только целое число!')

print('Список:', my_list)

#Длинна списка
list_length = len(my_list)
print('Длинна списка', list_length)

#Сумма списка. Метод списка.
total = sum(my_list)
print('Сумма списка:', total)

#Сумма списка. Метод цикла.
total = 0
for num in my_list:
    total += num
print('Сумма списка:', total)

#Четные элементы списка
even_nums = [num for num in my_list if num % 2 == 0]
print('Четные элементы списка:', even_nums)