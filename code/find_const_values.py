import pandas as pd

# Загрузка данных
output_file_path = 'CSE-CIC-IDS2018/stratified_sample_dataset.csv'
dataset = pd.read_csv(output_file_path)

# Поиск столбцов с постоянными значениями
constant_columns = [col for col in dataset.columns if dataset[col].nunique() == 1]
print("Столбцы с постоянными значениями:")
print(constant_columns)

# Удаление столбцов с постоянными значениями
dataset_cleaned = dataset.drop(columns=constant_columns)

# Сохранение очищенного DataFrame в новый CSV файл
cleaned_output_file_path = 'CSE-CIC-IDS2018/cleaned_dataset.csv'
dataset_cleaned.to_csv(cleaned_output_file_path, index=False)  # index=False, чтобы не сохранять индексы
print(f"Очищенный датасет успешно сохранён в {cleaned_output_file_path}")

