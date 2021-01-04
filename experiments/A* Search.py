class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = 0

    def calc_cost(self):
        count = 1
        current_parent = self.parent
        while current_parent.parent != None:
            count += 1
            current_parent = current_parent.parent
        return count
