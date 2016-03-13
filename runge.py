import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,10)
y = 1/(1+x*x)

# Polyfit fits a polynomial of degree len(x)
# Poly1d produces a polynomial that we can evaluate with the given coefficients
p =np.poly1d( np.polyfit(x, y, len(x) ))

xp = np.linspace(-5,5,100)
yexact = 1/(1+xp*xp)
plt.plot(x,y, 'o', xp, p(xp), '-', xp, yexact, '--r')
plt.show()

# Now let's try with just 20 data points
plt.figure()
x = np.linspace(-5,5,20)
y = 1/(1+x*x)

p20 =np.poly1d( np.polyfit(x, y, len(x) ))

plt.plot(x,y, 'o', xp, p20(xp), '-', xp, yexact, '--r')
plt.show()
