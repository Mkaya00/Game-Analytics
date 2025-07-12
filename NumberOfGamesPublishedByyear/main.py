import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("coolwarm")

data=pd.read_csv("../vgsales.csv")
data["Year"].value_counts().sort_index().plot(kind="bar",figsize=(15,5),edgecolor="black",align="center")
plt.title("Number of Games Published by Year",fontweight="bold")
plt.xlabel("Year",fontsize=13,fontweight="bold",labelpad=15)
plt.ylabel("Number of Games",fontsize=13,fontweight="bold",labelpad=15)
plt.xticks(rotation=45,ha="right",fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()

#plt.savefig("Number of Games Published by Year.png", dpi=300)

plt.show()


