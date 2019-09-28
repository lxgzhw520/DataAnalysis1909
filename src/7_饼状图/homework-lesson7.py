import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Some data

labels = 'SH', 'BJ', 'SZ', 'GD'
fracs = [20, 10, 30, 25]

explode = (0, 0, 0.05, 0)

plt.axes(aspect=1)

plt.pie(fracs, explode=explode, labels=labels, autopct='%.1f%%', shadow=True)

plt.show()