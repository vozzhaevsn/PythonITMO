#Список множеств
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

#Сравнение множеств на наличие пересечений
intersection_set = set1.intersection(set2) and  set2.intersection(set3) and set1.intersection(set3)

#Вывод пересекающегося значения
print(intersection_set)