
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

plt.figure(figsize=(8, 5))

plt.hist(df["Frequency"], bins=30, edgecolor="black")

plt.title("Customer Frequency Distribution")
plt.xlabel("Number of Purchases")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "visualizations/02_rfm_analysis/frequency_distribution.png",
    dpi=300
)

plt.show()
