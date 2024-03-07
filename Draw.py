import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("DataSilver.csv")
df1 = pd.read_csv("Data_Hand.csv")
print(df)
print(df1)
plt.plot(df['x6'])
plt.plot(df['x5'],color = 'pink')
plt.plot(df['x4'],color = 'blue')
plt.plot(df['x3'],color = 'brown')
plt.plot(df['x2'],color = 'green')
plt.plot(df['x1'],color = 'yellow')
plt.plot(df['y'],color = 'red')

plt.plot(df1['m5'],color = 'pink')
plt.plot(df1['m4'],color = 'blue')
plt.plot(df1['m3'],color = 'brown')
plt.plot(df1['m2'],color = 'green')
plt.plot(df1['m1'],color = 'yellow')
plt.plot(df1['n'],color = 'red')

plt.show()