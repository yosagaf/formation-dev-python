import matplotlib.pyplot as plt
import numpy as np

debut = 0.1
fin = 10
pas = 0.1

x = np.arange(debut, fin, pas)
f1 = np.log(x)
f2 = np.sqrt(x)

fig, ax = plt.subplots()
line1 = ax.plot(x, f1, 'r', label='f(x)=log(x)')
line2 = ax.plot(x, f2, 'm', label='f(x)=sqrt(x)')
ax.legend()
plt.show()
