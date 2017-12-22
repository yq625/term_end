import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = pd.read_table("tetrahymena.tsv")
f = pd. DataFrame(f)
data = f[(f['diameter']>19.2)]
data = data.groupby(['glucose','culture'])['conc','diameter'].mean()

data['log(conc)'] = np.log(data.conc)
data['log(diameter)'] = np. log(data.diameter)

x1 = data['log(diameter)']['glucose_yes']
x2 = data['log(diameter)']['glucose_no']
y1 = data['log(conc)']['glucose_yes']
y2 = data['log(conc)']['glucose_no']
plt.scatter(x1, y1, c='b', marker = 'x')
plt.scatter(x2, y2, c='r', marker = 's')
plt.show()