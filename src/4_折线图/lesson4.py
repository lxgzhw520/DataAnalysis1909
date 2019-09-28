import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()



date,open,close=np.loadtxt('000001.csv',delimiter=',',
                           converters={0:
                               mdates.strpdate2num(
                                       '%m/%d/%Y')},
                           skiprows=1,
                           usecols=(0,1,4),
                           unpack=True)


plt.plot_date(date,close,'y-')

plt.show()

plt.plot_date(date,close,'go')

plt.plot_date(date,close,'r--')

plt.show()

plt.plot(date, close, color='green', linestyle='dashed', marker='o',
     markerfacecolor='blue', markersize=12)

plt.show()


