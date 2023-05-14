import utils
import environment


def backtrack_search(env):
    best = {
        'cost': 0,
        'history': []
    }

    def recurse(state, history, total_cost):
        if env.done(state):
            if total_cost > best['cost']:
                best['cost'] = total_cost
                best['history'] = history
            return
        for action, newState, cost in env.possible_actions(state):
            if newState not in [a[1] for a in history]:
                recurse(newState, history + [(action, newState, cost)], total_cost + cost)
            else:
                continue

    recurse(env.get_state(), history=[(None, (0, 0), 0)], total_cost=0)
    return best['cost'], best['history']


problem = environment.Environment(3)
x, y = backtrack_search(problem)
hist = [a[1] for a in y]
utils.plot_path(grid_size=3, history=hist)
