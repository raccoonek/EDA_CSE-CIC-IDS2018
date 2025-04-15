import pandas as pd
from sklearn.model_selection import train_test_split

# Загрузка нормализованного датасета
output_file_path = 'CSE-CIC-IDS2018/normalized_dataset.csv'
dataset = pd.read_csv(output_file_path)

# Перемешивание строк в датасете
dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)

# Предположим, что 'Label' — это целевая переменная
X = dataset.drop(['Label'], axis=1)  # Признаки
y = dataset['Label']  # Целевая переменная

# Разделение данных на обучающую и валидационную выборки
# Пример: 80% для обучения и 20% для валидации
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Создание новых DataFrame для обучающей и валидационной выборок
train_dataset = pd.DataFrame(X_train, columns=X.columns)
train_dataset['Label'] = y_train.values

val_dataset = pd.DataFrame(X_val, columns=X.columns)
val_dataset['Label'] = y_val.values

# Сохранение выборок в отдельные файлы
train_dataset.to_csv('CSE-CIC-IDS2018/train_dataset.csv', index=False)
val_dataset.to_csv('CSE-CIC-IDS2018/val_dataset.csv', index=False)

# Вывод информации о размерах выборок
print(f"Размер обучающей выборки: {train_dataset.shape}")
print(f"Размер валидационной выборки: {val_dataset.shape}")


