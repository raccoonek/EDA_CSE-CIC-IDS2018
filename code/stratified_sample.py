import numpy as np
import pandas as pd

from loader import df0,df1,df2,df3,df4,df5,df6,df7,df8
N=10000
Strat_df0=df0.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False)) #Применение стратифицированной выборки к наборам данных
Strat_df1=df1.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
Strat_df2=df2.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
Strat_df3=df3.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
del df0,df1,df2,df3

Strat_df4=df4.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
Strat_df5=df5.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
Strat_df6=df6.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
del df4,df5,df6

Strat_df7=df7.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))
Strat_df8=df8.groupby('Label', group_keys=False).apply(lambda x: x.sample(min(N, len(x)), replace=False))

del df7,df8

final_dataset=pd.concat([Strat_df1,Strat_df2])
del Strat_df1,Strat_df2
final_dataset=pd.concat([final_dataset,Strat_df3])
del Strat_df3
final_dataset=pd.concat([final_dataset,Strat_df4])
del Strat_df4
final_dataset=pd.concat([final_dataset,Strat_df5])
del Strat_df5
final_dataset=pd.concat([final_dataset,Strat_df6])
del Strat_df6
final_dataset=pd.concat([final_dataset,Strat_df7])
del Strat_df7
final_dataset=pd.concat([final_dataset,Strat_df8])
del Strat_df8

final_dataset['Label'].value_counts()
print(final_dataset['Label'].value_counts())

# Сохранение final_dataset в CSV файл
output_file_path = 'CSE-CIC-IDS2018/stratified_sample_dataset.csv'  # Укажите желаемое имя файла
final_dataset.to_csv(output_file_path, index=False)  # index=False, чтобы не сохранять индексы
print(f"Данные успешно сохранены в {output_file_path}")
