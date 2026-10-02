
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/customer_segmentation.csv")

cluster_means = df.groupby("Cluster")[
    ["Recency", "Frequency", "Monetary"]
].mean()

cluster_means.plot(
    kind="bar",
    figsize=(9, 5),
    edgecolor="black"
)

plt.title("RFM Comparison Across Customer Clusters")
plt.xlabel("Customer Cluster")
plt.ylabel("Average Value")
plt.xticks(rotation=0)
plt.legend(title="RFM Metrics")

plt.tight_layout()

plt.savefig(
    "visualizations/03_clustering/rfm_cluster_comparison.png",
    dpi=300
)

plt.show()
