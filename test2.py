import pandas as pd

read_dat = pd.read_csv("chennai_reservoir_rainfall_made2.csv")
sum = 0
for val in read_dat["POONDI"]:
    sum += val

avg = sum/5647
print(avg)
