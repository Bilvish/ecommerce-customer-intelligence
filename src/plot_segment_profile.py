
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

profile = df.groupby("Segment")[
    ["Recency", "Frequency", "Monetary"]
].mean()

normalized = (
    profile - profile.min()
) / (
    profile.max() - profile.min()
)

normalized.plot(
    kind="bar",
    figsize=(9, 5),
    edgecolor="black"
)

plt.title("Normalized RFM Profile by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Normalized Average Value (0–1)")
plt.xticks(rotation=20)
plt.legend(title="RFM Metrics")

plt.tight_layout()

plt.savefig(
    "visualizations/03_clustering/normalized_rfm_profile.png",
    dpi=300
)

plt.show()
