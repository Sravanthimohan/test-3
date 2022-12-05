import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('mtcars.csv')
df["am"].plot(kind='bar')
plt.show()
