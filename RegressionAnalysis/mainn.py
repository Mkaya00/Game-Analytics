import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")
sns.set_palette("coolwarm")

data=pd.read_csv("/Users/mert/PycharmProjects/gameAnalyz/vgsales.csv")

plt.figure(figsize=(10, 6))

sns.regplot(data=data, x="Year", y="Global_Sales", scatter_kws={"alpha":0.5,"color":"red"}, line_kws={"color":"black"})

plt.title("Regression: Year vs Global Sales", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12, fontweight="bold")
plt.ylabel("Global Sales (millions)", fontsize=12, fontweight="bold")
plt.xticks(rotation=45, fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()
#plt.savefig("regression_year_global_sales.png")
plt.show()
