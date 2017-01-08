import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy
sympy.init_printing()
x = np.linspace(-5.0, 12.0, 100)
y = np.linspace(-4.0, 10.0, 100)
X, Y = np.meshgrid(x,y)
F = 12*X**5 + 36*Y**3 + 1600
fig = plt.figure()
plt.contour(X,Y,F,[0])
plt.title('Evolutionary Stable State', fontsize=10)
plt.xlabel('resource value', fontsize=10)
plt.ylabel('accuracy', fontsize=10)
fig.savefig('test.jpg')
plt.grid()
plt.show()

