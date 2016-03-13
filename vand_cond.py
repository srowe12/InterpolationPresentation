import numpy as np
import matplotlib.pyplot as plt

x_size = np.array([10,12,15,17,19,21])
c_list = []
for xs in x_size:
   x = np.linspace(0,2*np.pi,xs)
   y = np.sin(x)
   A = np.vander(x)
   c_list.append( np.linalg.cond(A) )

plt.semilogy(x_size,c_list,'o')
plt.title('Log Plot of Condition Number vs. Number of Samples')
plt.show()
