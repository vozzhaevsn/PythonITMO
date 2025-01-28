import re

file_way = r'C:\Users\Masha\Desktop\регулярные выражения\Логистика.txt'
with open(file_way, "r", encoding="cp1251") as file:
    text = file.read()
chapter_pattern = r"Глава\s\d+"
rubrication_pattern = r"\b\d+(\.\d+)+\b"
question_pattern = r"[А-Яа-яЁёA-Za-z0-9,;:()\\s-]+\?"

def search_and_display(pattern, text, description):
    matched = re.findall(pattern, text)  
    print(f"\n{description}")
    print(f"Общее количество совпадений: {len(matched)}")
    print(f"Первые 10 совпадений: {matched[:10]}")  

search_and_display(chapter_pattern, text, "Имена глав ")
search_and_display(rubrication_pattern, text, "Рубрикация ")
search_and_display(question_pattern, text, "Вопросы (кончающиеся на '?')")