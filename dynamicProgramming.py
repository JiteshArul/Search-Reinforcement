"""
Using Dynamic search: recurse over with cache to form a tree of entire possible situations and record the longest route
"""

def dynamic_search(env):
    cache = {}
    best = {
        'cost': 0,
        'history': []
    }

    # Gets in state to recurse over to the next state
    def recurse(state, history, total_cost):
        # if completed and record if the best cost is achieved
        if env.done(state):
            hist = [a[1] for a in history]
            if total_cost > best['cost']:
                best['cost'] = total_cost
                best['history'] = history
            return
        if state in cache:
            return cache[state]
        # loop over the possible states
        for action, newState, cost in env.possible_actions(state):
            if newState not in [a[1] for a in history]:
                cache[state] = recurse(newState, history + [(action, newState, cost)], total_cost + cost)
            else:
                continue

    recurse(env.get_start_state(), history=[(None, (0, 0), 0)], total_cost=0)
    return best['cost'], best['history']