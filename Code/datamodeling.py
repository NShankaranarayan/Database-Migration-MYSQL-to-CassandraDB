import pandas as pd

data1 = pd.read_csv("testdata.csv")
a=data1.columns.values.tolist()
print(data1)
n=2 #number of columns

for i in range(len(a)):
    print("i=",i)
    print("a[i]=",a[i])
    print(data1[a[i]][i])
