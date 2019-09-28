import numpy as np
import matplotlib.pyplot as plt
y=np.arange(1,5)
plt.plot(y,'cx--');
plt.plot(y+1,'kp:');
plt.plot(y+2,'mo-.');

plt.show()