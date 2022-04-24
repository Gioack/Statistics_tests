import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/master/adult.data.csv")
    race_count = df.race.value_counts()

    # # What is the average age of men?
    average_age_men = round(df.loc[df.sex == "Male", "age"].mean(),1)
    
    # What is the percentage of people who have a Bachelor's degree?
    people_number = float(race_count.sum())
    percentage_bachelors = round(float(df.loc[df["education"] == "Bachelors", "education"].count())/people_number*100,1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_array = df.loc[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"), "salary"]
    higher_education_rich_array = higher_education_array[higher_education_array == ">50K"]
    higher_education_rich = round(higher_education_rich_array.count()/higher_education_array.count()*100, 1)
    
    # What percentage of people without advanced education make more than 50K? 
    lower_education = df.salary.drop(higher_education_array.index)
    lower_education_rich = round(lower_education[lower_education == ">50K"].count()/lower_education.count()*100,1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours].salary
    rich_percentage = round(num_min_workers[num_min_workers == ">50K"].count()/num_min_workers.count()*100,1)
    
    # What country has the highest percentage of people that earn >50K?
    Rich_only = df[df["salary"] == ">50K"]
    percentage_rich = Rich_only["native-country"].value_counts().div(df["native-country"].value_counts(), axis='rows')*100
    highest_earning_country = percentage_rich[percentage_rich == percentage_rich.max()].index[0]
    highest_earning_country_percentage = round(percentage_rich[percentage_rich == percentage_rich.max()].values[0],1)
    
    # The most popular occupation for those who earn >50K in India.
    top_IN_occupation = Rich_only[Rich_only["native-country"] == "India"].occupation.value_counts().index[0]


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()
