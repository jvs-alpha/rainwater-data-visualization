import csv
import pandas as pd
import matplotlib.pyplot as plt

csv_dat = pd.read_csv("chennai_reservoir_rainfall_made1.csv")
read_dat = dict(csv_dat)
formed_dat = {"Date":[],"POONDI":[],"CHOLAVARAM":[],"REDHILLS":[],"CHEMBARAMBAKKAM":[]}
check = 0
on_read = None
for date in read_dat["Date"]:
    if date not in formed_dat["Date"]:
        formed_dat["Date"].append(date)
        for dat2 in read_dat["Date"]:
            if dat2 == 

    check += 1

#print(formed_dat)
print(check)
