import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


# Used to plot the path taken by the algorithms
def plot_path(grid_size, history):
    fig, ax = plt.subplots()

    # marking starting position with green
    ax.add_patch(Rectangle((0, 0), 1, 1, facecolor='green'))

    # marking end position with red
    ax.add_patch(Rectangle((grid_size - 1, grid_size - 1), 1, 1, facecolor='red'))

    ax.add_patch(Rectangle((0, 0), grid_size, grid_size, facecolor='none', edgecolor='black', alpha=1))
    x, y = zip(*history)

    # adding 0.5  to all values to make the path move through the middle
    x, y = [a + 0.5 for a in x], [a + 0.5 for a in y]
    plt.plot(x, y, linewidth=5)

    plt.xticks(np.arange(0, grid_size + 1, 1.0))
    plt.yticks(np.arange(0, grid_size + 1, 1.0))
    plt.grid()
    plt.show()
