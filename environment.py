class Environment:
    """
    Creation of Environment : A square maze made by a square matrix
        grid_size - length of rows and columns eg. 3X3 matrix maze
        start_pos - the start position of the maze
        end_pos - the end position of the maze
    """

    def __init__(self, grid_size=3):
        self.grid_size = grid_size
        self.start_pos = (0, 0)
        self.end_pos = (grid_size - 1, grid_size - 1)

    # To move the player to the reqired position
    def move(self, cur_state, i, j):
        row, col = cur_state
        if row + i in range(0, self.grid_size) and col + j in range(0, self.grid_size):
            return row + i, col + j
        else:
            return cur_state

    # Returns a list of all possible actions in the current state
    # Return form: (action , state after action, cost of the action)
    def possible_actions(self, cur_state):
        if self.done(cur_state):
            return []
        actions = []
        row, col = cur_state
        if row + 1 in range(0, self.grid_size):
            actions.append(('down', self.down(cur_state), 1))
        if row - 1 in range(0, self.grid_size):
            actions.append(('up', self.up(cur_state), 1))
        if col + 1 in range(0, self.grid_size):
            actions.append(('left', self.left(cur_state), 1))
        if col - 1 in range(0, self.grid_size):
            actions.append(('right', self.right(cur_state), 1))
        return actions

    # Moves the player one point towards the left
    def left(self, cur_state):
        return self.move(cur_state, 0, 1)

    # Moves the player one point towards the right
    def right(self, cur_state):
        return self.move(cur_state, 0, -1)

    # Moves the player one point towards down
    def down(self, cur_state):
        return self.move(cur_state, 1, 0)

    # Moves the player one point towards up
    def up(self, cur_state):
        return self.move(cur_state, -1, 0)

    # Returns the starting state of the player
    def get_start_state(self):

        return self.start_pos

    # Returns if the player has reached the end position or not
    def done(self, cur_state):
        row, col = cur_state
        if row == self.end_pos[0] and col == self.end_pos[1]:
            return True
        else:
            return False
