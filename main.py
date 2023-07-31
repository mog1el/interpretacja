import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('wyniki.xlsx')
plt.plot(df['∆x [mikrometr]'], df['średnia [mV]'])
plt.show()