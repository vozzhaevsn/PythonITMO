birth_day = int(input("Введите день рождения"))
birth_month = int(input("Введите месяц рождения"))
birth_year = int(input("Введите год рождения"))
if birth_month <= 3:
    print("Первый квартал")
elif birth_month <= 6:
    print("Второй квартал")
elif birth_month <= 9:
    print("Третий квартал")
elif birth_month <= 12:
    print("Четвертый квартал")
if (birth_year % 4 == 0 and birth_year % 100 != 0) or birth_year % 400 == 0:
    print("Високосный год")
else:
    print("Не високосный год")
to_day = int(input("Введите текущий день"))
to_month = int(input("Введите текущий месяц"))
to_year = int(input("Введите текущий год"))
days = (to_year - birth_year)*365.25+(to_month - birth_month)*30.33+(to_day - birth_day)
print(f"С твоего рождения прошло {int(days)} дней")