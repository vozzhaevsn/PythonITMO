import dask.dataframe as dd
import pandas as pd
import zipfile
from sqlalchemy import create_engine
import dask

# Настройки Dask
dask.config.set(scheduler="single-threaded", diagnostics="True")

# Распаковываем архив
archive_path = r"C:\Users\Masha\Downloads\recipes_full (1).zip"
with zipfile.ZipFile(archive_path, 'r') as z:
    z.extractall("recipes_full")  

# Создаем Dask DataFrame из всех CSV в папке "recipes"
df = dd.read_csv("recipes_full/*.csv", 
                 dtype={'minutes': 'float64', 'n_steps': 'float64'})  # Считываем все CSV в папке

# Отображение первых строк
print(df.head(5))

# Отображение последних строк (вычисляем данные)
print(df.tail(5))

# Метаинформация
print(f"Число блоков (npartitions): {df.npartitions}")
print("Типы столбцов:")
print(df.dtypes)
print("Первые 5 строк таблицы:")
print(df.head(5))
print("Последние 5 строк таблицы:")
print(df.tail(5))

# Количество строк в каждом блоке
partition_sizes = df.map_partitions(len).compute()
print("Количество строк в каждом блоке:", partition_sizes)

max_n_steps = df["n_steps"].max().compute()
print(f"Максимальное число шагов (n_steps): {max_n_steps}")

# Преобразуем даты в формат datetime
df["submitted"] = dd.to_datetime(df["submitted"])

# Выделяем месяц и подсчитываем количество отзывов
reviews_by_month = df.groupby(df["submitted"].dt.month).size().compute()
print("Количество отзывов по месяцам:")
print(reviews_by_month)

# Наиболее активный пользователь
most_active_user = df["contributor_id"].value_counts().idxmax().compute()
print(f"Пользователь, отправивший больше всего рецептов: {most_active_user}")

first_recipe = df["submitted"].min().compute()
last_recipe = df["submitted"].max().compute()
print(f"Самый первый рецепт отправлен: {first_recipe}")
print(f"Самый последний рецепт отправлен: {last_recipe}")

median_time = df["minutes"].median_approximate().compute()
mean_steps = df["n_steps"].mean().compute()

# Создаём строку соединения с базой SQLite
database_uri = "sqlite:///recipes.db"  
df.to_sql("recipes", database_uri, if_exists="replace", index=False)

# Фильтруем рецепты
filtered_df = df[(df["minutes"] < median_time) & (df["n_steps"] < mean_steps)]

filtered_df.to_csv("filtered_recipes.csv", index=False, single_file=True)  # Для сохранения в один файл