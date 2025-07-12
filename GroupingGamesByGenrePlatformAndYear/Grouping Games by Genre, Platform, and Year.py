import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../vgsales.csv")
df = df.dropna(subset=['Year'])
df['Year'] = df['Year'].astype(int)

genres = df['Genre'].unique()
print("Available genres:")
for g in genres:
    print("-", g)

user_genre = input("Choose a genre from the list above: ")


filtered = df[df['Genre'].str.lower() == user_genre.lower()]

if filtered.empty:
    print(f"No data found for genre: {user_genre}")
else:

    grouped = filtered.groupby('Year').size().reset_index(name='Game_Count')


    plt.figure(figsize=(10, 6),)
    plt.plot(grouped['Year'], grouped['Game_Count'], marker='o', color='darkblue')
    plt.title(f'Number of {user_genre.title()} Games Released by Year',fontweight="bold")
    plt.xlabel('Year',fontweight="bold",labelpad=20,fontsize=13)
    plt.ylabel('Number of Games',fontweight="bold",labelpad=20,fontsize=13)
    plt.xticks(rotation=45, ha="right", fontweight="bold")
    plt.yticks(fontweight="bold")
    plt.tight_layout()
    plt.show()