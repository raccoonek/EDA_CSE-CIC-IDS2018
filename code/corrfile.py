import pandas as pd

cleaned_output_file_path = 'CSE-CIC-IDS2018/cleaned_dataset.csv'
dataset = pd.read_csv(cleaned_output_file_path)

Y_Labels = dataset['Label'] #Splitting the Xi and Yi to apply the Permutation Importance model and identify the importanat features to further apply model
X_data = dataset.drop(['Label','Timestamp'],axis=1)

from matplotlib import pyplot as plt
import seaborn as sns
fig= plt.figure(figsize=(100,100))
sns.heatmap(X_data.corr(), annot=False,cmap="YlGnBu")

plt.show()


def get_correlation_high(X_data, threshold):  # Findout the features with the correlation value greater than the threshold
    corr_col = set()
    corrmat = X_data.corr()
    for i in range(len(corrmat.columns)):
        for j in range(i):
            if abs(corrmat.iloc[i, j]) > threshold:
                colname = corrmat.columns[i]
                corr_col.add(colname)
    return corr_col


corelated_features = get_correlation_high(X_data, 0.95)  # spot the highly co realted features in the dataset

corr = list(corelated_features)
print(corr)
for i in corr:  # dropping the highly corelated features from the dataset
    dataset.drop(labels=[i], axis=1, inplace=True)

# Сохранение очищенного DataFrame в новый CSV файл
cleaned_output_file_path = 'CSE-CIC-IDS2018/ready_dataset.csv'
dataset.to_csv(cleaned_output_file_path, index=False)

print(dataset.shape)
print(dataset.columns)