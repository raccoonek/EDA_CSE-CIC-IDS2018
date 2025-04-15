import pandas as pd

# Загружаем данные
output_file_path = 'CSE-CIC-IDS2018/dataset.csv'  # Замените на путь к вашему файлу
dataset = pd.read_csv(output_file_path, low_memory=False)

# Функция для получения уникальных строковых значений из заданного столбца
def get_unique_string_values(column):
    # Фильтруем только строки и получаем уникальные значения
    return column[column.apply(lambda x: isinstance(x, str))].unique()

# Выводим уникальные строковые значения из указанных столбцов
unique_values_7 = get_unique_string_values(dataset.iloc[:, 7])
unique_values_10 = get_unique_string_values(dataset.iloc[:, 10])
unique_values_29 = get_unique_string_values(dataset.iloc[:, 29])
unique_values_36 = get_unique_string_values(dataset.iloc[:, 36])

# Печатаем уникальные строковые значения
print("Уникальные строковые значения из столбца 7:")
print(unique_values_7)

print("\nУникальные строковые значения из столбца 10:")
print(unique_values_10)

print("\nУникальные строковые значения из столбца 29:")
print(unique_values_29)

print("\nУникальные строковые значения из столбца 36:")
print(unique_values_36)
