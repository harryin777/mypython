import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler

cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names=cols)
df.head()

df["class"] = (df["class"] == "g").astype(int)

for label in cols:
    plt.hist(df[df["class"] == 1][label], color='blue', label='gmma', alpha=0.7, density=True)
    plt.hist(df[df["class"] == 0][label], color='red', label='hadron', alpha=0.7, density=True)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()

train, valid, test = np.split(df.sample(frac=1), [int(0.6 * len(df)), int(0.8 * len(df))])


def scale_dataset(dataframe, oversample=False):
    X = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    if oversample:
        ros = RandomOverSampler()
        X, y = ros.fit_resample(X, y)

    data = np.hstack((X, np.reshape(y, (-1, 1))))
    return data, X, y


train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)
test, X_test, y_test = scale_dataset(test, oversample=False)

# test test test
X = df[df.columns[:-1]].values
y = df[df.columns[-1]].values
scaler = StandardScaler()
print(X)
print("-" * 20)
X = scaler.fit_transform(X)
print(X)
data = np.hstack((X, np.reshape(y, (-1, 1))))
print("-" * 20)
print(data)
print("-" * 20)
print(np.reshape(y, (-1, 2)))
print("-" * 20)
print(y)

# KNN
knn_model = KNeighborsClassifier(n_neighbors=1)
knn_model.fit(X_train, y_train)
KNeighborsClassifier(n_neighbors=1)

y_pred = knn_model.predict(X_test)
print(classification_report(y_test, y_pred))
