
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

avg_spending = (
    df.groupby("Segment")["Monetary"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

avg_spending.plot(kind="bar", edgecolor="black")

plt.title("Average Customer Spending by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Monetary Value")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "visualizations/04_business_insights/average_spending_by_segment.png",
    dpi=300
)

plt.show()
