import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walks()

# Plot the points in the walk
plt.style.use('classic')
fix, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()