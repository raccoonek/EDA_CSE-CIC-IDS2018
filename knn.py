import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

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

# Обучение модели KNN
model = KNeighborsClassifier(n_neighbors=5)  # Вы можете изменить количество соседей
model.fit(X_train, Y_train)

# Предсказание на тестовой выборке
Y_pred = model.predict(X_test)

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
