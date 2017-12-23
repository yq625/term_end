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
[slope1, intercept1] = list(np.polyfit(x1,y1,deg = 1))
[slope2, intercept2] = list(np.polyfit(x2,y2,deg = 1))
# print(type(slope1))
def abline(slope, intercept, symbol):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, symbol)

abline(slope1, intercept1, "-")
abline(slope2, intercept2, "--")
plt.show()



