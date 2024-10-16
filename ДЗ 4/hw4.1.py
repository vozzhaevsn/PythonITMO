# Определим допустимые символы для email и проверку на номера телефонов
email_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-@")
phone_chars = set("0123456789()+- ")

emails = set()
phones = set()

input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read().splitlines()
    
    for line in content:
        words = line.split()
        for word in words:
            # Проверка, является ли слово электронной почтой
            if '@' in word and all(c in email_chars for c in word) and word.count('@') == 1:
                at_index = word.index('@')
                if '.' in word[at_index:]:
                    emails.add(word)

            # Проверка, является ли слово номером телефона
            if all(c in phone_chars for c in word):
                cleaned_word = ''.join(c for c in word if c.isdigit())
                if len(cleaned_word) in [10, 11]:  # Проверяем, что длина 10 или 11
                    phones.add(cleaned_word)

# Запись результатов в файл
with open(output_file, 'w', encoding='utf-8') as file:
    file.write("Найденные электронные почты:\n")
    for email in emails:
        file.write(email + '\n')
    file.write("\nНайденные номера телефонов:\n")
    for phone in phones:
        file.write(phone + '\n')
