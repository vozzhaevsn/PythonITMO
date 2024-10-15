# Определение функции
def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # Читаем все строки из файла

        line_count = len(lines)  # Подсчет количества строк
        word_count = 0  # Подсчет количества слов
        char_count = 0  # Подсчет количества символов
        longest_word = ""  # Для хранения самого длинного слова

        for line in lines:
            words = line.split()  # Разделяем строку на слова
            word_count += len(words)  # Увеличиваем количество слов
            char_count += len(line)  # Увеличиваем количество символов
            for word in words:
                if len(word) > len(longest_word):  # Проверяем, длиннее ли текущее слово самого длинного
                    longest_word = word

        longest_word_length = len(longest_word)  # Длина самого длинного слова

        return {
            'lines': line_count,
            'words': word_count,
            'characters': char_count,
            'longest_word': longest_word,
            'longest_word_length': longest_word_length
        }

    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Путь к вашему файлу
result = analyze_file('test.txt')

# Вывод результата
print(result)
