import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(10))
y = 170-x
noise = np.random.randn(10)
plt.plot(x,y+noise,'o')
plt.title('Weekly Weight Measurements on 500 Calorie Daily Deficit')
plt.xlabel('Week')
plt.ylabel('Weight (lbs)')
#plt.show()

p  = np.poly1d(np.polyfit(x,y,1))
plt.plot(x,p(x),'r')
plt.show()
