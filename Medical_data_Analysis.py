import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/master/medical_examination.csv",index_col=0)

# Add 'overweight' column
df['overweight'] = df.weight/((df.height/100)**2)
df.loc[df["overweight"]<=25, "overweight"] = 0
df.loc[df["overweight"]>25, "overweight"] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"]>1, "cholesterol"] = 1
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"]>1, "gluc"] = 1
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
# Clean the data
#print(df.loc[((df['height'] <= Quantile_25_height)
               # | (df['height'] >= Quantile_975_height) ), "ap_hi"].count())
# print(df.loc[df['ap_lo'] > df['ap_hi'], "ap_hi"].count())
Filter_pressure  = (df['ap_lo'] <= df['ap_hi'])
# print(Filter_pressure.sum())
# print(Filter_pressure.count())
df = df[Filter_pressure ]

# print(df.loc[df['ap_lo'] > df['ap_hi'], "ap_hi"].count())

Quantile_25_height = df["height"].quantile(0.025)
Quantile_975_height = df["height"].quantile(0.975)
Quantile_25_weight = df["weight"].quantile(0.025)
Quantile_975_weight = df["weight"].quantile(0.975)

print(df.loc[df['height'] < Quantile_25_height, "ap_hi"].count())
# print(Filter_height.sum())
Filter_height = ((df['height'] >= Quantile_25_height)
                & (df['height'] <= Quantile_975_height) )
df = df[Filter_height]
print(Quantile_25_height)
Filter_weight = ((df['weight'] >= Quantile_25_weight)
                & (df['weight'] <= Quantile_975_weight))
df = df[Filter_weight]

# print(df.loc[((df['height'] <= Quantile_25_height)
                # (df['height'] >= Quantile_975_height) ), "ap_hi"].count())

print(df.loc[df['height'] < Quantile_25_height, "ap_hi"].count())
print(df.loc[df['height'] > Quantile_975_height, "ap_hi"].count())
print(df.loc[df['weight'] < Quantile_25_weight, "ap_hi"].count())
print(df.loc[df['weight'] > Quantile_975_weight, "ap_hi"].count())

# Draw Heat Map
def draw_heat_map():
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
