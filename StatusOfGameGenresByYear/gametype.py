import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("coolwarm")



gnr=data=pd.read_csv("../vgsales.csv")

genre_year = gnr.groupby(["Year", "Genre"]).size().unstack(fill_value=0)


genre_year.plot(kind="bar", stacked=True, figsize=(15,7), colormap='Paired')
plt.title("StatusOfGameGenresByYear", fontsize=16, fontweight="bold")
plt.xlabel("Year",fontsize=13,fontweight="bold",labelpad=15)
plt.ylabel("NumberOfGames",fontsize=13,fontweight="bold",labelpad=15)
plt.legend(title="Genre",title_fontsize=12,
bbox_to_anchor=(1.05, 1), loc='upper left',prop={'size': 10})
plt.xticks(rotation=45,ha="right",fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()
#plt.savefig("StatusOfGameGenresByYear.png", dpi=300)
plt.show()