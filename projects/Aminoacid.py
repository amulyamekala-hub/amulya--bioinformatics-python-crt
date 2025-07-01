import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
'''
#problem:Given protien sequences,compute the amino acid compositionand display it as a pie chart.
'''
#----data---
data = {
    "ProteinID": [f"P{i}" for i in range(1, 13)],
    "Sequence": [
        "MAGDTPLKNQV", "AAAGGTTCCSS", "MLVITGVAGGL", "WQQVVSSGGA",
        "FFTLLVVAAK", "GGGGSSSAAA", "CCDDDEEEFF", "MMNNPPQQRR",
        "KKTTSSTTGG", "VVVVAAAAFFF", "LLLIIIHHHHH", "SSSTTTGGGAA"
    ]     
}
df=pd.DataFrame(data)
#---composition-----------------------------------------
all_seq="".join(df["Sequence"])
counts=Counter(all_seq)
lables,sizes=zip(*sorted(counts.items()))
#---visual------------------------------------------
cmap=plt.colormaps.get_cmap("tab20")
colors=[cmap(i) for i in range(len(lables))]
plt.figure(figsize=(9,9))
wedges,_, autotexts = plt.pie(
    sizes,
    labels=lables,
    colors=colors,
    explode=[0.5]*len(lables),
    startangle=140,
    autopct=lambda pct: f"{pct:.1f}%\n({int(pct/100*sum(sizes))})",
     textprops=dict(color="black", fontsize=10)
)
plt.legend(
    wedges,
    [f"{aa}: {cnt}" for aa, cnt in counts.items()],
    title="Amino acids (count)",
    bbox_to_anchor=(1,0.5),
    loc="center left",
    fontsize=9
)
plt.title("Amino.Acid Composition from 12 Protiens",
          fontsize=14,fontweight="bold",color="darkblue")
plt.tight_layout()
plt.show()