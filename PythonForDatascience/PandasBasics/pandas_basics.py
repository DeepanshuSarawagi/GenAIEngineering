import pandas as pd

df = pd.read_csv('../ReadWriteFiles/songs_sample_generated.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
song_details = df[['title', "artist", "year"]]
print(song_details)
print(song_details.iloc[0,0])

"""Method to find unique values in a column"""
unique_artists = df['artist'].unique()
print(unique_artists)

"""How to extract data based on a condition"""
songs_after_2000 = df[df['year'] > 2000]
print(songs_after_2000)

"""Write the filtered data to a new CSV file"""
songs_after_2000.to_csv('../ReadWriteFiles/songs_after_2000.csv', index=False)

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)
print(df)