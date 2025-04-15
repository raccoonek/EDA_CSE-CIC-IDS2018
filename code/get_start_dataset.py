import numpy as np
import pandas as pd

from loader import df0,df1,df2,df3,df4,df5,df6,df7,df8

final_dataset = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8])
del df0,df1,df2,df3,df4,df5,df6,df7,df8



# Сохранение final_dataset в CSV файл
output_file_path = 'CSE-CIC-IDS2018/start_dataset.csv'  # Укажите желаемое имя файла
final_dataset.to_csv(output_file_path, index=False)  # index=False, чтобы не сохранять индексы
print(f"Данные успешно сохранены в {output_file_path}")
