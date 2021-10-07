import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new waks, as long as the program is active
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walks()

    # Plot the points in the walk
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(11, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last point.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100 )
    
    # Remove the axis.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break