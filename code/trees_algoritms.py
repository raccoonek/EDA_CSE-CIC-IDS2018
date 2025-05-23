import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import tim_mem as t
import time
# Чтение данных
filename = 'CSE-CIC-IDS2018/normalized_dataset.csv'
data = pd.read_csv(filename)

# Перемешивание данных
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Разделение на признаки и метки
X = data.iloc[:, :-1]  # Все колонки, кроме последней
Y = data.iloc[:, -1]   # Последняя колонка

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Замер времени на обучение
start_time = time.time()

# Выбор метода построения деревьев
# Для CART
base_model_cart = DecisionTreeClassifier(criterion='gini', random_state=4)

# Для C4.5, используйте библиотеку python-c45 (не забудьте установить)
# from c45 import C45Classifier
# base_model_c45 = C45Classifier()

# Для C5.0, используйте библиотеку pyC5.0 (не забудьте установить)
# from pyC50 import C50
# base_model_c50 = C50()


# Обучение модели с использованием бэггинга
model = BaggingClassifier(base_estimator=base_model_cart, n_estimators=20, random_state=4)  # Используйте базовую модель по вашему выбору
model.fit(X_train, Y_train)

# Вывод метрик во время обучения
print(f"Training Time: {time.time() - start_time:.4f} seconds")
t.print_memory_usage()
t.print_cpu_usage()

# Замер времени на предсказание
start_time = time.time()
Y_pred = model.predict(X_test)
prediction_time = time.time() - start_time
print(f"Prediction Time: {prediction_time:.4f} seconds")

# Вычисление метрик
print(classification_report(Y_test, Y_pred))
conf_mat = confusion_matrix(Y_test, Y_pred)

# Визуализация матрицы ошибок
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Anomaly', 'Normal'], yticklabels=['Anomaly', 'Normal'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
