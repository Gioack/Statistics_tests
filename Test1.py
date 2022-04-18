import pandas as pd
import matplotlib.pyplot as plt
data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)
print(df['Name'].value_counts())
df[["Name","Age"]].boxplot(by="Name", figsize=(10,6))
plt.show()