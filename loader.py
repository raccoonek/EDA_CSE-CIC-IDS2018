
import pandas as pd #loading the obtained web attack datset from Kaggles
# each csv hold the diffrent type of DDOS attacks collected on diffrent dates

df0=pd.read_csv('CSE-CIC-IDS2018/02-14-2018_modified.csv',sep=';', on_bad_lines='skip', encoding='utf-8')
df1=pd.read_csv('CSE-CIC-IDS2018/02-15-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df2=pd.read_csv('CSE-CIC-IDS2018/02-16-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df3=pd.read_csv('CSE-CIC-IDS2018/02-21-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df4=pd.read_csv('CSE-CIC-IDS2018/02-22-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df5=pd.read_csv('CSE-CIC-IDS2018/02-23-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df6=pd.read_csv('CSE-CIC-IDS2018/02-28-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df7=pd.read_csv('CSE-CIC-IDS2018/03-01-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
df8=pd.read_csv('CSE-CIC-IDS2018/03-02-2018_modified.csv',sep=',', on_bad_lines='skip', encoding='utf-8')
