import pandas as pd

output_file_path = 'CSE-CIC-IDS2018/train_dataset.csv'
dataset = pd.read_csv(output_file_path)

un = dataset['Label'].value_counts()
print(un)