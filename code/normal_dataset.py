import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Загрузка датасета
output_file_path = 'CSE-CIC-IDS2018/dataset.csv'
dataset = pd.read_csv(output_file_path)

# Проверка на наличие NaN и бесконечных значений
print("Проверка на NaN:")
print(dataset.isna().sum())  # Количество NaN в каждом столбце

print("\nПроверка на бесконечные значения:")
print((dataset == float('inf')).sum())  # Количество бесконечных значений в каждом столбце
print((dataset == float('-inf')).sum())  # Количество отрицательных бесконечных значений в каждом столбце

# Удаление или замена NaN и бесконечных значений
dataset.replace([float('inf'), float('-inf')], pd.NA, inplace=True)  # Заменяем бесконечные значения на NaN
dataset.dropna(inplace=True)  # Удаляем строки с NaN

# Создание экземпляра MinMaxScaler
scaler = MinMaxScaler()

# Выделение признаков для нормализации (исключая целевую переменную)
X_data = dataset.drop(['Label'], axis=1)  # Убедитесь, что 'Label' — это правильное название столбца

# Применение нормализации
X_normalized = scaler.fit_transform(X_data)

# Создание нового DataFrame с нормализованными данными
normalized_df = pd.DataFrame(X_normalized, columns=X_data.columns)

# Если нужно, добавьте целевую переменную обратно
normalized_df['Label'] = dataset['Label'].values

# Сохранение нормализованного датасета (если нужно)
normalized_df.to_csv('CSE-CIC-IDS2018/normalized_dataset.csv', index=False)

# Вывод первых нескольких строк нормализованного датасета
print(normalized_df.head())
