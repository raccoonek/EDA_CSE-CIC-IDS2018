import numpy as np
import pandas as pd

from loader import df0,df1,df2,df3,df4,df5,df6,df7,df8

final_dataset = pd.concat([df0,df1,df2,df3,df4,df5,df6,df7,df8])
del df0,df1,df2,df3,df4,df5,df6,df7,df8

# Удаление столбцов с постоянными значениями
final_dataset_cleaned = final_dataset.drop(['Bwd PSH Flags', 'Bwd URG Flags', 'Fwd Byts/b Avg', 'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg', 'Bwd Pkts/b Avg', 'Bwd Blk Rate Avg','Fwd Act Data Pkts', 'Pkt Size Avg', 'Idle Max', 'Active Max', 'CWE Flag Count', 'SYN Flag Cnt', 'Subflow Bwd Pkts', 'Fwd Pkt Len Std', 'Fwd IAT Max', 'Fwd Header Len', 'Subflow Fwd Byts', 'Bwd Header Len', 'Pkt Len Std', 'Subflow Bwd Byts', 'TotLen Fwd Pkts', 'Subflow Fwd Pkts', 'Idle Min', 'TotLen Bwd Pkts', 'ECE Flag Cnt', 'Bwd IAT Min', 'Bwd Seg Size Avg', 'Fwd IAT Tot', 'Bwd Pkt Len Std', 'Fwd IAT Min', 'Fwd Seg Size Avg'],axis=1)
del final_dataset

final_dataset_cleaned.replace(to_replace=['Infilteration','Bot','DoS attacks-GoldenEye','DoS attacks-Hulk','DoS attacks-Slowloris','SSH-Bruteforce','FTP-BruteForce','DDOS attack-HOIC','DoS attacks-SlowHTTPTest','DDOS attack-LOIC-UDP','Brute Force -Web','Brute Force -XSS','SQL Injection'],value=0,inplace=True) #encoding the Anamalous and Normal values as 0 and 1 to visualize
final_dataset_cleaned.replace(to_replace=['Benign'],value=1,inplace=True)


# Сохранение final_dataset в CSV файл
output_file_path = 'CSE-CIC-IDS2018/dataset.csv'  # Укажите желаемое имя файла
final_dataset_cleaned.to_csv(output_file_path, index=False)  # index=False, чтобы не сохранять индексы
print(f"Данные успешно сохранены в {output_file_path}")


