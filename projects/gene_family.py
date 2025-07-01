# write a python program to count how many genes belong to each family from the given data and visualize in using barchart
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}
df = pd.DataFrame(data)
family_counts = df['Family'].value_counts()
print("Gene Family Counts:")
print(family_counts)
family_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Genes per Family')
plt.xlabel('Gene Family')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()