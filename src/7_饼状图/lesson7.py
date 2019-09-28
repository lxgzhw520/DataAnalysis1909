import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Some data

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]

explode = (0, 0.05, 0, 0)

# Make square figures and axes

plt.axes(aspect=1)


explode = (0, 0.05, 0, 0)

#plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

plt.pie(fracs, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)



plt.show()