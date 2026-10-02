
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

revenue = df.groupby("Segment")["Monetary"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))

revenue.plot(kind="bar", edgecolor="black")

plt.title("Revenue Contribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Revenue")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "visualizations/04_business_insights/segment_revenue.png",
    dpi=300
)

plt.show()
