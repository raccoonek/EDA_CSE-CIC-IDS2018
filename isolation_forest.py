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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=45)

# Фильтрация X_train по метке Y_train = 1
X_train_filtered = X_train[Y_train == 1]

# Количество частей для кросс-валидации
n_splits = 2
split_size = len(X_train) // n_splits

# Инициализация переменной для отслеживания precision
precision = 0
start = 2000
step = 500
# Инициализация модели изолированного леса
model = IsolationForest(n_estimators=start, random_state=10, warm_start=True, max_features=45, bootstrap=True, max_samples = 10000000)

# Начальное значение n_estimators
n_estimator = start

while precision < 0.95:
    model.set_params(n_estimators=n_estimator)

    # Случайный выбор индексов для обучения
    random_indices = np.random.choice(len(X_train), size=split_size * (n_splits - 1), replace=False)
    X_train_random = X_train.iloc[random_indices]

    model.fit(X_train_random)

    # Получение подмножества для тестирования (все, кроме выбранных)
    X_test_random = X_train.drop(X_train.index[random_indices])
    Y_test_random = Y_train.drop(Y_train.index[random_indices])

    # Предсказание на тестовой выборке
    Y_pred = model.predict(X_test_random)

    # Преобразование предсказаний: -1 (аномалия) и 1 (норма) в 0 и 1
    Y_pred = [0 if x == -1 else 1 for x in Y_pred]

    # Вычисление метрик
    report = classification_report(Y_test_random, Y_pred, output_dict=True)
    precision = report['0.0']['precision']  # Получаем precision для класса 0 (атака)

    print(f"Current Precision: {precision:.4f}, деревья: {n_estimator} ")

    # Увеличиваем n_estimators для следующей итерации
    n_estimator += step

# Предсказание на тестовой выборке
Y_pred = model.predict(X_test)
# Преобразование предсказаний: -1 (аномалия) и 1 (норма) в 0 и 1
Y_pred = [0 if x == -1 else 1 for x in Y_pred]

# После завершения цикла выводим финальную матрицу ошибок
conf_mat = confusion_matrix(Y_test, Y_pred)

# Визуализация матрицы ошибок
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Anomaly', 'Normal'],
            yticklabels=['Anomaly', 'Normal'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
