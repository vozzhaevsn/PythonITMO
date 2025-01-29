import zipfile
import pandas as pd
import os
from sqlalchemy import create_engine
zip_file_path = r"C:\Users\vipya\recipes_full.zip"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall()
print(zip_ref.infolist())
file_path = r"C:\Users\vipya\.vscode\PythonITMO-1\Data\recipes_full\recipes_full_0.csv"
df = pd.read_csv(file_path)
print(df.head())
max_n_steps = df['n_steps'].max()
print(f"Максимальное значение в столбце n_steps: {max_n_steps}")
df1=df.info()
df['submitted'] = pd.to_datetime(df['submitted'])
monthly_reviews = df['submitted'].dt.to_period('M').value_counts().sort_index()
print("Количество отзывов по месяцам:\n", monthly_reviews.head())
contributor = df['contributor_id'].value_counts().idxmax()
print("Пользователь, отправлявший рецепты чаще всех:", contributor)
first_recipe = df.loc[df['submitted'].idxmin()]
last_recipe = df.loc[df['submitted'].idxmax()]
print("Самый первый рецепт:")
print(first_recipe)
print("\nСамый последний рецепт:")
print(last_recipe)
ingredients = df['n_ingredients'].median()
minutes = df['minutes'].median()
print("Медиана по количеству ингредиентов:", ingredients)
print("Медиана по времени приготовления:", minutes)
simplest_recipe = df.sort_values(by=['n_ingredients', 'minutes', 'n_steps']).iloc[0]

print("Самый простой рецепт:",simplest_recipe)
engine = create_engine('sqlite:///recipes.db')

df.to_sql('recipes', con=engine, if_exists='replace', index=False)
mean_n_steps = df['n_steps'].mean()
filtered_recipes = df[(df['minutes'] < minutes) & (df['n_steps'] < mean_n_steps)]
filtered_csv_path = os.path.abspath('filtered_recipes.csv')
filtered_recipes.to_csv(filtered_csv_path, index=False)
print("Отфильтрованные рецепты сохранены в:", filtered_csv_path)
