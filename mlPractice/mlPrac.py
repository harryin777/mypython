import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cols = ["sepal length", "sepal width", "petal length", "petal width", "class"]
df = pd.read_csv("iris.data", names=cols)
# print(df.head())
# print(df["class"].unique())

count = 0
for item in df["class"]:
    # print(item)
    if item == 'Iris-setosa':
        df["class"][count] = 1
    elif item == 'Iris-versicolor':
        df["class"][count] = 2
    else:
        df["class"][count] = 3
    count = count + 1

for lable in cols:
    plt.hist(df[df["class"] == 1][lable], color='blue', label='gmma', alpha=0.7, density=True)
    plt.hist(df[df["class"] == 2][lable], color='red', label='gmma', alpha=0.7, density=True)
    plt.title(lable)
    plt.ylabel("Probability")
    plt.xlabel(lable)
    plt.legend()
    plt.show()
