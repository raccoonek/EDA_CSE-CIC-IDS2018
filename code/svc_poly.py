import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
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

# Разделение данных на обучающую и тестовую выборки (70% обучающая, 30% тестовая)
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3, random_state=42)

# Разделение временной выборки на валидационную и тестовую (50% валидационная, 50% тестовая из 30%)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)

# Создание пайплайна с PCA и SVC
pipeline = Pipeline([
    ('pca', PCA(n_components=0.95)),  # Сохраняем 95% дисперсии
    ('svc', SVC(kernel='poly', random_state=42))
])

# Определение гиперпараметров для настройки
param_grid = {
    'svc__degree': range(1, 6),  # Степени от 1 до 5
    'svc__C': [0.1, 1, 10, 100],  # Разные значения C
}

# Настройка GridSearchCV для кросс-валидации
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# Обучение модели с использованием GridSearchCV
grid_search.fit(X_train, Y_train)

# Получение лучшей модели и результатов
best_model = grid_search.best_estimator_
best_score = grid_search.best_score_
best_params = grid_search.best_params_

print(f"Best Parameters: {best_params}")
print(f"Best Cross-Validation Accuracy: {best_score:.4f}")

# Предсказание на тестовой выборке с лучшей моделью
Y_test_pred = best_model.predict(X_test)

# Вычисление метрик для тестовой выборки
print("Test Classification Report:")
print(classification_report(Y_test, Y_test_pred))
conf_mat = confusion_matrix(Y_test, Y_test_pred)

# Визуализация матрицы ошибок
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Anomaly', 'Normal'],
            yticklabels=['Anomaly', 'Normal'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
