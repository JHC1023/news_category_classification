import pandas as pd
import datetime

categories = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']

file_path = './crawling_data/'

df_headlines = pd.DataFrame()

for category in categories :
    file_name = 'news_headlines_{}_20250416.csv'.format(category)
    load_data = pd.read_csv(file_path + file_name)
    df_headlines = pd.concat([df_headlines, load_data], ignore_index=True, axis=0)

df_headlines.info()

print(df_headlines.head())
print(df_headlines.tail())
print(df_headlines['category'].unique())

df_headlines.to_csv('./crawling_data/news_headlines_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)