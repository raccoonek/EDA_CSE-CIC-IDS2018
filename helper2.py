import pandas as pd

# Загрузка данных из CSV файла
file_path = 'CSE-CIC-IDS2018/02-28-2018_modified.csv'
df = pd.read_csv(file_path, sep=',', on_bad_lines='skip', encoding='utf-8')

# Проверка наличия столбца 'Label'
if 'Label' in df.columns:
    # Подсчет количества вхождений каждого уникального значения в столбце 'Label'
    label_counts = df['Label'].value_counts()

    # Вывод результатов
    print("Количество вхождений различных типов в столбце 'Label':")
    print(label_counts)
else:
    print("Столбец 'Label' не найден в DataFrame.")