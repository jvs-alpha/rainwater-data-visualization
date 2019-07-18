'''
THIS PROGRAM IS USED FOR CHANGING THE DATE FORMAT OF THE "Date" COLUMN IN THE CSV
TO JUST A NUMBER "YEAR"
'''
import pandas as pd
csv_dat = pd.read_csv("chennai_reservoir_rainfall.csv")
check = 0
# This loop will read the date of the values on the "Date" column
# and reevaluate it as just the year
for i in csv_dat["Date"]:
    sub_date = i.split("-")
    csv_dat["Date"][check] = sub_date[2]
    check += 1

csv_dat.to_csv(r"chennai_reservoir_rainfall_made1.csv")
