import pandas as pd
import matplotlib.pyplot as plt

# Load customer dataset
df = pd.read_csv("data/customer_segmentation.csv")

# Create histogram
plt.figure(figsize=(8, 5))

plt.hist(df["Recency"], bins=20, edgecolor="black")

# Add title and labels
plt.title("Customer Recency Distribution")
plt.xlabel("Recency (Days)")
plt.ylabel("Number of Customers")

# Improve layout
plt.tight_layout()

# Save visualization
plt.savefig(
    "visualizations/02_rfm_analysis/recency_distribution.png",
    dpi=300
)

# Display chart
plt.show()