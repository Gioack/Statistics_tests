import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv", parse_dates=['date'])

# Clean data
df = df.loc[df["value"] > df["value"].quantile(q=0.025)]
df = df.loc[df["value"] < df["value"].quantile(q=0.975)]

def draw_line_plot():
    df.plot(x="date",y="value",color='red')     
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.ylabel("Page Views")
    plt.xlabel("Date")
    plt.show()

def draw_bar_plot():
    df_bar = df.copy()
    df_bar["date"] = df_bar["date"].astype(str).str[:-3]
    df_bar["year"] = df_bar["date"].str[:4]
    df_bar["date"] = df_bar["date"].str[5:8]
    df_bar["date"] = df_bar["date"].astype(int)
    df_bar.sort_values(by='date')

    sns.barplot(x="year",y="value",hue="date",data=df_bar,ci=None,palette="Paired")
    plt.legend(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], title="Months")
    plt.ylabel("Average Page Views")
    plt.xlabel("Years")
    plt.show()

def draw_box_plot():
    df_box = df.copy()
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)

    fig, (ax1,ax2) = plt.subplots(1,2,sharey=True)
    sns.boxplot(x="year",y="value",data=df_box,ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    sns.boxplot(x="month",y="value",data=df_box,ax=ax2)
    ax2.set_ylabel("")
    ax1.set_ylabel("Page Views")
    plt.show()
