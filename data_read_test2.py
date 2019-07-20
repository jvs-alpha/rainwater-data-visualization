import pandas as pd
import matplotlib.pyplot as plt

csv_dat = pd.read_csv("chennai_reservoir_rainfall_made1.csv")
read_dat = dict(csv_dat)
mod_dat = {"Date":[],"POONDI":[],}
for date in read_dat["Date"]:
    if date not in mod_dat["Date"]:
        mod_dat["Date"].append(date)

sum = 0
for date in mod_dat["Date"]:
    for check in range(0,5647):
        if read_dat["Date"][check] == date:
            sum += read_dat["POONDI"][check]
    mod_dat["POONDI"].append(sum)
    sum = 0
mod_dat = pd.DataFrame(mod_dat)
mod_dat.to_csv("chennai_reservoir_rainfall_made2.csv")
