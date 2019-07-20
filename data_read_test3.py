import pandas as pd
import matplotlib.pyplot as plt

read_dat = pd.read_csv("chennai_reservoir_rainfall_made2.csv")
read_dat.plot(kind="bar",x="Date")
plt.show()
