import pandas as pd
import matplotlib.pyplot as pltdf = pd.read_csv('data.csv')
monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales Analysis')
plt.savefig('output.png')
plt.show()
