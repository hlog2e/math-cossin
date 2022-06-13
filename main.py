import math
import numpy as np
import matplotlib

x = np.linspace(-5, 5, 100)
sin = np.sin(x)
cos = np.cos(x)

plt.plot(x, sin, label='sine')
plt.plot(x, cos, label='cosine')
plt.legend()

