#Создание Словаря
person1 = {"a": 1, "b": 2, "c": 3}

#
person2 = {}

for char, num in person1.items():
    person2[num] = char
    print(person2)