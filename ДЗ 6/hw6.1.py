import string

def get_word_weight(word):
    weight = sum(ord(char) for char in word)
    return weight

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid][1] == target:
            return mid
        elif sorted_list[mid][1] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def search_word(user_input):
    user_input_weight = get_word_weight(user_input)
    index = binary_search(sorted_weights, user_input_weight)
    
    if index is not None:
        found_word = sorted_weights[index]
        print(f"Слово '{found_word[0]}' найдено! Вес: {found_word[1]}, Индекс: {index}.")
    else:
        print(f"Слово '{user_input}' не найдено.")

# Ввод слов вручную
words = input("Введите слова через пробел: ").split()

# Получение весов слов и сортировка
weights = {word: get_word_weight(word) for word in words}
sorted_weights = sorted(weights.items(), key=lambda x: x[1])
print("\nОтсортированный список слов по весам:")
for item in sorted_weights:
    print(f"{item[0]} : {item[1]}")

# Поиск слова
user_input = input("\nВведите слово для поиска: ")
search_word(user_input.strip())