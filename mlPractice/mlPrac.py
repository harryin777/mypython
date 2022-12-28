import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cols = ["sepal length", "sepal width", "petal length", "petal width", "class"]
df = pd.read_csv("iris.data", names=cols)
# print(df.head())
# print(df["class"].unique())

for item in df["class"]:
    # print(item)
    if item == 'Iris-setosa':
        item = 1
    elif item == 'Iris-versicolor':
        item = 2
    else:
        item = 3

print(df.head())
