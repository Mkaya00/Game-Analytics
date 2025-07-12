import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_palette("coolwarm")


data=pd.read_csv("../vgsales.csv")
corr_matrix = data.corr(numeric_only=True)


plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, square=True)

plt.title("Correlation Matrix of Numerical Features", fontweight="bold", fontsize=14)
plt.xticks(rotation=45, ha="right", fontweight="bold")
plt.yticks(fontweight="bold")

plt.tight_layout()
#plt.savefig("correlation_matrix.png")
plt.show()