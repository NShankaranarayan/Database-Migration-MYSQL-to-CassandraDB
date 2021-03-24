from cassandra.cluster import Cluster
import pandas as pd
import numpy

def beginop(table):
    cluster=Cluster()
    cassandra_cluster = cluster.connect('test_keyspace')
    df = pd.read_csv("testdata.csv")
    a = df.columns.values.tolist()
    b=df.values.tolist()
    col=len(a)
    row=len(df)
    currentrow=[]
    print(df.head())
    print("Constructing Query --/")
    #query construction
    tname=table
    query="Insert into "+tname
    #("Insert into emp2(id,name) values(%s,%s)", [s,p])
    #temp="Insert into emp2(id,name) values("+s+","+p+")"
    pk=0
    while(pk<=row-1):
        query="Insert into "+tname+"("
        currentrow=[]
        for i in range(col):
            if (i == col - 1):
                query = query + a[i] + ') values('
            else:
                query = query + a[i] + ','
        i=1
        integer=numpy.int64(5)
        string=str(1)

        for i in range(col):
            currentrow.append(df[a[i]][pk])


        for i in range(col):
            if(i==col-1) and (type(currentrow[i])==type(integer)):
                query=query+str(currentrow[i])
                query=query+")"
            elif (i != col - 1) and (type(currentrow[i]) == type(integer)):
                query = query + str(currentrow[i])
                query = query + ","
            elif (i == col - 1) and (type(currentrow[i]) == type(string)):
                query = query +"'"+str(currentrow[i])+"'"
                query = query + ")"
            elif (i != col - 1) and (type(currentrow[i]) == type(string)):
                query = query +"'"+str(currentrow[i])+"'"
                query = query + ","
        print(query)
        cassandra_cluster.execute(query)
        pk=pk+1
    return
#tohere



"""
data1 = pd.read_csv("testdata.csv")
print(data1)
for i in range(len(data1)):
    s=data1['id'][i]
    p=data1['name'][i]
    cassandra_cluster.execute("Insert into emp2(id,name) values(%s,%s)", [s,p])
"""