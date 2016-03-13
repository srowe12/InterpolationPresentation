import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,10)
y = np.sin(x)

plt.plot(x,y,'o')
plt.title('Wow Some Points!')

x_fit = np.linspace(0,2*np.pi,1000)
y_fit = np.sin(x_fit)
plt.figure()
plt.plot(x,y,'o')
plt.plot(x_fit,y_fit,'g')
plt.title('Interpolation! I pass through the data points')


y += .05*np.random.randn(10)

plt.figure()
plt.plot(x,y,'o')
plt.plot(x_fit,y_fit,'g')
plt.title('Well I tried to pass through the data')
plt.show()


