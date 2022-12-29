import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names=cols)
df.head()

df["class"]=(df["class"]=="g").astype(int)

# for label in cols:
#     plt.hist(df[df["class"] == 1][label], color='blue', label='gmma', alpha=0.7, density=True)
#     plt.hist(df[df["class"] == 0][label], color='red', label='hadron', alpha=0.7, density=True)
#     plt.title(label)
#     plt.ylabel("Probability")
#     plt.xlabel(label)
#     plt.legend()
#     plt.show()

# train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

X = df[df.columns[:-1]].values
y = df[df.columns[-1]].values
scaler = StandardScaler()
print(X)
print("-"*20)
X = scaler.fit_transform(X)
print(X)
data = np.hstack((X, np.reshape(y, (-1, 1))))
print("-"*20)
print(data)
print("-"*20)
print(np.reshape(y, (-1, 2)))
print("-"*20)
print(y)
