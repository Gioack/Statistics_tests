import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
        df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv")
        
        df.plot("Year","CSIRO Adjusted Sea Level",label="Rise in sea level")

        res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
        plt.plot(range(1880,2051), res.intercept + res.slope*range(1880,2051), 'r', label="Sea level using 1880-2013's slope until 2050",color="Green")

        df_after_2000 = df.loc[df["Year"]>2000, :]
        res1 = linregress(df_after_2000["Year"], df_after_2000["CSIRO Adjusted Sea Level"])
        plt.plot(range(2000,2051), res1.intercept + res1.slope*range(2000,2051), 'r', label="Sea level using 2000-2013's slope until 2050")

        plt.title("Rise in Sea Level")
        plt.ylabel("Sea Level (inches)")
        plt.xlabel("Year")
        plt.legend()
        plt.show()
draw_plot()