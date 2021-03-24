import pandas as pd
import numpy

df = pd.read_csv("testdata.csv")
a = df.columns.values.tolist()
b=df.values.tolist()
col=len(a)
row=len(df)
currentrow=[]
print(df)

#query construction
tname="emp2("
query="Insert into "+tname
#("Insert into emp2(id,name) values(%s,%s)", [s,p])
#temp="Insert into emp2(id,name) values("+s+","+p+")"
for i in range(col):
    if(i==col-1):
        query=query+a[i]+') values('
    else:
        query=query+a[i]+','
i=1
integer=numpy.int64(5)
string=str(1)
while(i==1):
    for i in range(col):
        currentrow.append(df[a[i]][0])


    for i in range(col):
        if(i==col-1) and (type(currentrow[i])==type(integer)):
            query=query+str(currentrow[i])
            query=query+")"
        elif (i != col - 1) and (type(currentrow[i]) == type(integer)):
            query = query + str(currentrow[i])
            query = query + ","
        elif (i == col - 1) and (type(currentrow[i]) == type(string)):
            query = query +'"'+str(currentrow[i])+'"'
            query = query + ")"
        elif (i != col - 1) and (type(currentrow[i]) == type(string)):
            query = query +'"'+str(currentrow[i])+'"'
            query = query + ","
    print(query)

    i=i-1