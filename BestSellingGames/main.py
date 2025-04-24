import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set_style("whitegrid")
sns.set_palette("coolwarm")

data=pd.read_csv("/Users/mert/PycharmProjects/gameAnalyz/vgsales.csv")
top10 = data.groupby("Name")["Global_Sales"].sum().sort_values(ascending=False).head(10)

top10.sort_values().plot(kind="barh",figsize=(15,5),edgecolor="black",align="center",color="red")

plt.title("Top 10 Best-Selling Video Games",fontweight="bold")
plt.xlabel("Sales(in millions)",fontsize=13,fontweight="bold",labelpad=15)
plt.ylabel("Games",fontsize=13,fontweight="bold",labelpad=15)
plt.xticks(rotation=45,ha="right",fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()

#plt.savefig("BestSelling.png",dpi=300)

plt.show()