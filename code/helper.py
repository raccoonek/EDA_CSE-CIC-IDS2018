import pandas as pd
import re

# Список файлов и их разделителей
file_info = [
    ('CSE-CIC-IDS2018/02-14-2018.csv', ';'),
    ('CSE-CIC-IDS2018/02-15-2018.csv', ','),
    ('CSE-CIC-IDS2018/02-16-2018.csv', ','),
    ('CSE-CIC-IDS2018/02-21-2018.csv', ','),
    ('CSE-CIC-IDS2018/02-22-2018.csv', ','),
    ('CSE-CIC-IDS2018/02-23-2018.csv', ','),
    ('CSE-CIC-IDS2018/02-28-2018.csv', ','),
    ('CSE-CIC-IDS2018/03-01-2018.csv', ','),
    ('CSE-CIC-IDS2018/03-02-2018.csv', ',')
]

# Функция для очистки DataFrame от символов, занимающих более одного байта
def clean_dataframe(df):
    results = []
    for row_index, row in df.iterrows():
        for col_index, value in enumerate(row):
            if isinstance(value, str):
                # Удаляем все символы, которые не являются однобайтовыми
                cleaned_value = re.sub(r'[^\x00-\x7F]', '', value)

                if cleaned_value == '':
                    df.iat[row_index, col_index] = 0  # Заменяем на 0, если строка пустая
                else:
                    df.iat[row_index, col_index] = cleaned_value
                    results.append((row_index, col_index))
    return df

# Обработка каждого файла
for file_path, sep in file_info:
    try:
        # Читаем CSV-файл в DataFrame
        df = pd.read_csv(file_path, sep=sep, on_bad_lines='skip', encoding='utf-8')

        # Очищаем DataFrame от символов, занимающих более одного байта
        cleaned_df = clean_dataframe(df)

        # Выводим результаты
        #if cleaned_results:
         #   for row, col in cleaned_results:
          #      print(f"Символы, занимающие более одного байта, удалены в файле '{file_path}' в строке {row + 1}, столбце {col + 1}.")
        #else:
         #   print(f"Не найдено символов, занимающих более одного байта, в файле '{file_path}'.")

        # Сохраняем измененный DataFrame в новый CSV файл
        modified_file_path = file_path.replace('.csv', '_modified.csv')
        cleaned_df.to_csv(modified_file_path, sep=sep, index=False, encoding='utf-8')
        print(f"Измененный файл сохранен как '{modified_file_path}'.")

    except Exception as e:
        print(f"Ошибка при обработке файла '{file_path}': {e}")
