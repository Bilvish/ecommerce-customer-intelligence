
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

segment_counts = df["Segment"].value_counts()

plt.figure(figsize=(8, 5))

segment_counts.plot(kind="bar", edgecolor="black")

plt.title("Customer Segmentation Distribution")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "visualizations/03_clustering/customer_segment_distribution.png",
    dpi=300
)

plt.show()
