
def turn_right_finder(maze, start_point, exit_point, give_up):
    current_point = start_point
    while maze.is_exit_point(current_point):
        current_point = maze.get_next_position(current_point, 'e')


class Maze:

    def solve(self, strategy, give_up):
        return strategy.solve(self, self._enter_point, self._exit_point, give_up)


class Adder:

    def __init__(self, addition):
        self._addition = addition

    def __call__(self, param):
        return self._addition + param


add5 = Adder(5)
add5(6)


m = Maze()
m.solve(turn_right_finder)