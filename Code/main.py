import importcsv as ipcsv
import Exportcsv as excsv

def start():
    print("--------------------------------------------------")
    print("Enter the target table name for retriving::")
    tname=input()
    print("Exporting Table -t/")
    excsv.startop(tname)
    print("Export successful -t/")
    print("--------------------------------------------------")
    print("Enter the target table name for storing::")
    tname2= input()
    print("Importing Table to Cassandra Distributed DB -t/")
    ipcsv.beginop(tname2)
    print("--------------------------------------------------")
    print("Export Successfully Completed")
    print("--------------------------------------------------")
start()