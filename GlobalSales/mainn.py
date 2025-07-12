import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




sns.set_style("whitegrid")
sns.set_palette("coolwarm")

data=pd.read_csv("../vgsales.csv")
yearly_sales = data.groupby("Year")["Global_Sales"].sum()

yearly_sales.plot(kind="line",figsize=(15,5),marker="o",color="darkblue")

plt.title("Global Sales By Year",fontweight="bold")
plt.xlabel("Year",fontsize=13,fontweight="bold",labelpad=15)
plt.ylabel("Global Sales (in millions)",fontsize=13,fontweight="bold",labelpad=15)
plt.xticks(rotation=45,ha="right",fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()

#plt.savefig("Global Sales.png",dpi=300)

plt.show()