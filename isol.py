import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Чтение данных
filename = 'CSE-CIC-IDS2018/normalized_dataset.csv'
data = pd.read_csv(filename)

# Перемешивание данных
data = data.sample(frac=1, random_state=4).reset_index(drop=True)

# Разделение на признаки и метки
X = data.iloc[:, :-1]  # Все колонки, кроме последней
Y = data.iloc[:, -1]  # Последняя колонка

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=45)

# Фильтрация X_train по метке Y_train = 1
X_train_norm = X_train[Y_train == 1]
X_test_norm = X_test[Y_test == 1]
Y_test_norm = Y_test[Y_test==1]

X_norm = pd.concat([X_train, X_train_norm, X_train_norm, X_train_norm], ignore_index=True)
X_train_random = X_norm.sample(frac=1, random_state=44).reset_index(drop=True)

X_t_norm = pd.concat([X_test, X_test_norm, X_test_norm, X_test_norm], ignore_index=True)
Y_t_norm = pd.concat([Y_test, Y_test_norm, Y_test_norm, Y_test_norm], ignore_index=True)
X_test_random = X_t_norm.sample(frac=1, random_state=44).reset_index(drop=True)
Y_test_random = Y_t_norm.sample(frac=1, random_state=44).reset_index(drop=True)

# Количество частей для кросс-валидации
n_splits = 1
split_size = len(X_train) // n_splits

# Инициализация переменной для отслеживания precision
precision = 0
start = 20

# Инициализация модели изолированного леса
model = IsolationForest(n_estimators=start, contamination=0.08, random_state=10, max_features=45, max_samples = 211675470)

model.fit(X_train_random)

# Предсказание на тестовой выборке
Y_pred = model.predict(X_test_random)
# Преобразование предсказаний: -1 (аномалия) и 1 (норма) в 0 и 1
Y_pred = [0 if x == -1 else 1 for x in Y_pred]


# Вычисление метрик
report = classification_report(Y_test_random, Y_pred, output_dict=True)

precision = report['0.0']['recall']  # Получаем precision для класса 0 (атака)

print(f"Current Precision: {precision:.4f}, деревья: {start} ")


# После завершения цикла выводим финальную матрицу ошибок
conf_mat = confusion_matrix(Y_test_random, Y_pred)

# Визуализация матрицы ошибок
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Anomaly', 'Normal'], yticklabels=['Anomaly', 'Normal'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
