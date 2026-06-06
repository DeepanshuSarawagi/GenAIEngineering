import pandas as pd

df = pd.read_csv('../ReadWriteFiles/songs_sample_generated.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
song_details = df[['title', "artist", "year"]]
print(song_details)