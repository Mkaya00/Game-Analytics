### Video Game Sales Dataset Correlation Analysis

**About the Dataset**

This analysis was conducted on the numerical features of the vgsales.csv dataset. The selected features are:
Rank, Year, NA_Sales, EU_Sales, JP_Sales, Other_Sales, and Global_Sales.
The aim is to investigate the relationships (correlations) between these numerical variables.

**Correlation Findings**

Global Sales Correlations:

There is a very high positive correlation between Global_Sales and NA_Sales (0.94) as well as EU_Sales (0.90).
Other regions also show positive correlations: Other_Sales (0.75) and JP_Sales (0.61).
Interpretation: NA and EU regional sales are strong indicators for predicting global sales.

Rank Correlations:

Rank has a negative correlation with sales variables:

Global_Sales: -0.43

NA_Sales: -0.40

EU_Sales: -0.38

Interpretation:

As Rank decreases (closer to 1st place), sales increase, meaning the most popular games have the highest sales.

Year Correlations:

The Year variable shows very weak or no significant correlation with sales or rank (values like 0.18, -0.09).

Interpretation:

Sales success does not strongly depend on the year of release.
Regional Sales Correlations:
There is a strong correlation between NA_Sales and EU_Sales (0.77).
JP_Sales behaves more independently compared to other regions (with lower correlations like 0.45, 0.44, 0.29).

**Overall Conclusions**

Best predictors for Global Sales: NA_Sales and EU_Sales.

Top-ranked games (lower Rank value) generally have higher sales.

Japanese market acts more independently and should be analyzed separately.

Time factor (Year) is not a major determinant of sales.
