import pandas as pd

output_file_path = 'CSE-CIC-IDS2018/dataset.csv'
dataset = pd.read_csv(output_file_path)

dataset = dataset.drop(['Timestamp'],axis=1)

dataset.to_csv(output_file_path,index=False)