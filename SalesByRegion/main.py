import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stil ayarları
sns.set_style("whitegrid")
sns.set_palette("coolwarm")

# Veri setini oku
data=pd.read_csv("../vgsales.csv")

# Bölgesel satışların toplamını al
regional_sales = data[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].sum()

# Grafik çizimi
plt.figure(figsize=(10, 5))
regional_sales.plot(kind="bar", edgecolor="black", align="center",color="orange")

plt.title("Total Sales by Region", fontweight="bold")
plt.xlabel("Region", fontsize=13, fontweight="bold", labelpad=15)
plt.ylabel("Sales (millions)", fontsize=13, fontweight="bold", labelpad=15)
plt.xticks(rotation=45, ha="right", fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()
#plt.savefig("SalesByRegion.png", dpi=300)
plt.show()