import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import time
import psutil

# Функция для замера использования ресурсов
def print_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()

    print(f"Peak Memory Usage: {mem_info.vms / (1024 ** 2):.2f} MB")  # Пиковое использование памяти

def print_cpu_usage():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")  # Процент использования CPU


#Чтение данных
filename = 'CSE-CIC-IDS2018/normalized_dataset.csv'
data = pd.read_csv(filename)

#Перемешивание данных
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

#Разделение на признаки и метки
X = data.iloc[:, :-1] # Все колонки, кроме последней
Y = data.iloc[:, -1] # Последняя колонка

#Разделение данных на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)


# Замер времени на обучение
start_time = time.time()

#Обучение модели SGDClassifier
model = SGDClassifier(loss='hinge', max_iter=10000000, random_state=42) # Используем SGD для SVM
model.fit(X_train, Y_train)


# Вывод метрик во время обучения
print(f"Training Time: {time.time() - start_time:.4f} seconds")
print_memory_usage()
print_cpu_usage()

# Замер времени на предсказание
start_time = time.time()
#Предсказание на тестовой выборке
Y_pred = model.predict(X_test)
prediction_time = time.time() - start_time
print(f"Prediction Time: {prediction_time:.4f} seconds")

#Вычисление метрик
print(classification_report(Y_test, Y_pred))
conf_mat = confusion_matrix(Y_test, Y_pred)

#Визуализация матрицы ошибок
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Anomaly', 'Normal'], yticklabels=['Anomaly', 'Normal'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()