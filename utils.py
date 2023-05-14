import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle


def plot_path(grid_size, history):
    fig, ax = plt.subplots()

    ax.add_patch(Rectangle((0, 0), 1, 1, facecolor='green'))
    ax.add_patch(Rectangle((grid_size - 1, grid_size - 1), 1, 1, facecolor='red'))
    ax.add_patch(Rectangle((0, 0), grid_size, grid_size, facecolor='none', edgecolor='black', alpha=1))
    x, y = zip(*history)
    x, y = [a + 0.5 for a in x], [a + 0.5 for a in y]
    plt.plot(x, y, linewidth=5)
    plt.xticks(np.arange(0, grid_size + 1, 1.0))
    plt.yticks(np.arange(0, grid_size + 1, 1.0))
    plt.grid()
    plt.show()
