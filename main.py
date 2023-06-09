from backpropagation import backtrack_search
from dynamicProgramming import dynamic_search
import environment as env
import utils

problem = env.Environment(3)
x, y = backtrack_search(problem)
hist = [a[1] for a in y]
utils.plot_path(grid_size=3, history=hist)
x, y = dynamic_search(problem)
hist = [a[1] for a in y]
utils.plot_path(grid_size=3, history=hist)
