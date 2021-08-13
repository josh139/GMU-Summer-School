import pandas as pd
from matplotlib import pyplot as plt
 
poke = pd.read_csv("Pokemon.csv")

''' 
poke.boxplot(column='Total', by='Generation') # 1.
plt.show()
'''

plt.bar(column='Total', by='Type 1')
plt.show()
