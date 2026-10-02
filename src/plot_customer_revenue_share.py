
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

customer_share = (
    df["Segment"].value_counts(normalize=True) * 100
)

revenue_share = (
    df.groupby("Segment")["Monetary"].sum()
    / df["Monetary"].sum() * 100
)

comparison = pd.DataFrame({
    "Customer Share": customer_share,
    "Revenue Share": revenue_share
}).fillna(0)

comparison.plot(
    kind="bar",
    figsize=(9, 5),
    edgecolor="black"
)

plt.title("Customer Share vs Revenue Contribution")
plt.xlabel("Customer Segment")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=20)
plt.legend()

plt.tight_layout()

plt.savefig(
    "visualizations/04_business_insights/customer_revenue_share.png",
    dpi=300
)

plt.show()
