from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

uni = np.random.uniform(size =1500)
exp = np.random.exponential(size =1500)
gam = np.random.gamma(1,size =1500)
norm = np.random.normal(size =1500)

for c, z , dist in zip(['r', 'g', 'b', 'y'], [30, 30, 30, 30], [uni,exp,gam,norm]):
    xs = np.arange(1500)
    ys = dist

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()