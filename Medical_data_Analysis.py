import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/master/medical_examination.csv",index_col=0)

df['overweight'] = df.weight/((df.height/100)**2)
df.loc[df["overweight"]<=25, "overweight"] = 0
df.loc[df["overweight"]>25, "overweight"] = 1

# the following normalizes data by making 0 always good and 1 always bad.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"]>1, "cholesterol"] = 1
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"]>1, "gluc"] = 1

def draw_cat_plot():
    
    df_cat = pd.melt(df.loc[:, "cholesterol":"overweight"], id_vars=["cardio"])
    df_cat_0cardio = df_cat.loc[df_cat["cardio"] == 0, "variable":"value"]
    df_cat_1cardio = df_cat.loc[df_cat["cardio"] == 1, "variable":"value"]
    df_cat_0cardio.sort_values('variable', inplace=True)
    df_cat_1cardio.sort_values('variable', inplace=True)
    fig, (ax1,ax2) = plt.subplots(1,2,sharey=True,figsize=[12,8])
    fig.subplots_adjust(wspace=0)
    ax1.set_title("Cardio-0")
    ax2.set_title("Cardio-1")
    sns.countplot(x="variable",hue = "value",data=df_cat_0cardio,ax=ax1)
    sns.countplot(x="variable",hue = "value",data=df_cat_1cardio,ax=ax2)
    ax1.set_ylabel("Total")
    ax2.set_ylabel("")
    ax1.get_legend().set_visible(False)
    ax2.get_legend().set_visible(False)
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper left')
    plt.show()

    return fig


Filter_pressure  = (df['ap_lo'] <= df['ap_hi'])
df = df[Filter_pressure]

Quantile_25_height = df["height"].quantile(0.025)
Quantile_975_height = df["height"].quantile(0.975)
Quantile_25_weight = df["weight"].quantile(0.025)
Quantile_975_weight = df["weight"].quantile(0.975)

Filter_height = ((df['height'] >= Quantile_25_height)
                & (df['height'] <= Quantile_975_height) )
df = df[Filter_height]
Filter_weight = ((df['weight'] >= Quantile_25_weight)
                & (df['weight'] <= Quantile_975_weight))
df = df[Filter_weight]

def draw_heat_map():
    
    corr = df.corr()
    corr = corr.round(2)
    
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=[12,8])
    sns.heatmap(corr,mask=mask,annot=True,ax=ax)
    plt.show()
    return fig

