#Создаем функцию, которая включает список путей к файлам и логический парамерт для пределения нужно ли записывать в файл(по умолчанию True)
def merge_files(file_paths, write_to_file=True):
     #Создаем переменную для хранения объединенного содержимого
    merge_content = ''
    #Создаем цикл, который будет читать каждый путь
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as file:
            merge_content += file.read() + '\n'  # Объединяем содержимое файлов
    #Создаем уловие записи содержимого в файл
    if write_to_file:
        with open('all_file.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(merge_content)  # Записываем в новый файл
    #Возвращаем объединенное содержимое в виде строки
    return merge_content  # Возвращаем объединенное содержимое как строку
#Исполнене функции. Задаем список файлов для объединения
file_list = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
result = merge_files(file_list)  # Записывает в файл по умолчанию
print(result)  # Печатает объединенное содержимое
