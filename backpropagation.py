"""
Using Backtrack search: recurse over to form a tree of entire possible situations and record the longest route
"""


def backtrack_search(env):
    best = {
        'cost': 0,
        'history': []
    }

    # Gets in state to recurse over to the next state
    def recurse(state, history, total_cost):
        # if completed and record if the best cost is achieved
        if env.done(state):
            if total_cost > best['cost']:
                best['cost'] = total_cost
                best['history'] = history
            return
        # loop over the possible states
        for action, newState, cost in env.possible_actions(state):
            if newState not in [a[1] for a in history]:
                recurse(newState, history + [(action, newState, cost)], total_cost + cost)
            else:
                continue

    recurse(env.get_start_state(), history=[(None, (0, 0), 0)], total_cost=0)
    return best['cost'], best['history']
