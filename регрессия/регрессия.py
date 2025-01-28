import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error, explained_variance_score
from sklearn.model_selection import train_test_split

script_dir = os.path.dirname(os.path.abspath(__file__))
x_path = r"C:\Users\Masha\.vscode\homework\регрессия\6_x.csv"
y_path = r"C:\Users\Masha\.vscode\homework\регрессия\6_y.csv"

x = np.loadtxt(x_path, delimiter=',')
y = np.loadtxt(y_path, delimiter=',')
print("Данные успешно загружены!")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

def calculate_metrics(model_name, y_true, y_pred):
    return {
        'Model': model_name,
        'R2_Score': r2_score(y_true, y_pred),
        'MSE': mean_squared_error(y_true, y_pred),
        'EVS': explained_variance_score(y_true, y_pred)
    }

metrics = []

for i in range(x.shape[1]):
    reg = LinearRegression()
    reg.fit(x_train[:, i].reshape(-1, 1), y_train)
    y_pred = reg.predict(x_test[:, i].reshape(-1, 1))
    metrics.append(calculate_metrics(f'Linear Regression Feature {i+1}', y_test, y_pred))

reg_multi = LinearRegression()
reg_multi.fit(x_train, y_train)
y_pred_multi = reg_multi.predict(x_test)

metrics.append(calculate_metrics('Multiple Linear Regression', y_test, y_pred_multi))

for degree in [2, 3]:
    for i in range(x.shape[1]):
        poly = PolynomialFeatures(degree=degree)
        x_train_poly = poly.fit_transform(x_train[:, i].reshape(-1, 1))
        x_test_poly = poly.transform(x_test[:, i].reshape(-1, 1))

        reg_poly = LinearRegression()
        reg_poly.fit(x_train_poly, y_train)
        y_pred_poly = reg_poly.predict(x_test_poly)
        metrics.append(calculate_metrics(f'Polynomial Regression (Degree {degree}) Feature {i+1}', y_test, y_pred_poly))

results = pd.DataFrame(metrics)
results_path = os.path.join(script_dir, 'regression_metrics_summary.csv')
results.to_csv(results_path, index=False)

print(f' Метрики сохранены в файл: {results_path}')