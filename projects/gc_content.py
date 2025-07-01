'''
#Problem:Given DNA sequences, calculate the GC content 
# of each and plot it as a histogram
'''
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)

# Function to calculate GC content
def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return (gc / len(seq)) * 100

# Apply the function to each sequence
df['GC_Content'] = df['Sequence'].apply(gc_content)
print(df[['GeneID', 'Sequence', 'GC_Content']])

# Plot histogram of GC content
plt.hist(df['GC_Content'], color='skyblue')
plt.title('GC Content Histogram')
plt.xlabel('GC Content (%)')
plt.ylabel('Frequency')
plt.show()
# write a python program to count how many genes belong to each family from the given data and visualize in using barchart