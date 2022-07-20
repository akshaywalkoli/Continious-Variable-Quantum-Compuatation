from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np
m = 1
w = 10
h= 6.62606957*(10**-34.0)
fig, ax = plt.subplots(nrows=1, ncols=1, num=0, figsize=(16, 8),
                       subplot_kw={'projection': '3d'})
gridY, gridX = np.mgrid[-4:4:33 * 1j, -4:4:33 * 1j]         # this solves the 2d error of the Z axis



W_xp = ((4*m*w)/h)**0.5 * (np.exp((-1)*((gridX**2 + gridY**2)+((2*m*w)/2))))

pSurf = ax.plot_surface(gridX, gridY, W_xp, rstride=1, cstride=1, cmap='rainbow')
fig.colorbar(pSurf)
plt.show()
