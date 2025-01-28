mylist = ['apple', 'balloon', 'castle', 'dreams', 'forest', 'gravity', 'horizon', 'island', 'jungle', 'kingdom',
                'legend', 'mountain', 'nebula', 'ocean', 'paradise']
def calculate_weight(word):
    return sum(ord(char) for char in word)

word_weights = []
for word in mylist:
    weight = calculate_weight(word)
    word_weights.append((word, weight))


word_weights_sorted = sorted(word_weights, key=lambda item: item[1])


print("Список слов и их весов (отсортированный):")
user_word = input("Введите слово для поиска: ")
user_weight = calculate_weight(user_word)


weights_only = [weight for _, weight in word_weights_sorted]  

low = 0
high = len(weights_only) - 1
found = False
index = -1

while low <= high:
    mid = (low + high) // 2
    if weights_only[mid] == user_weight:
        found = True
        index = mid
        break
    elif weights_only[mid] < user_weight:
        low = mid + 1
    else:
        high = mid - 1

if found:
    word = word_weights_sorted[index][0]  # Получаем слово по индексу
    print(f"Слово '{word}' найдено с весом {user_weight} на индексе {index}.")
else:
    print("Слово не найдено.")
