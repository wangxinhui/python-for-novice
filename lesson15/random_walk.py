from random import choice
class RandomWalk():
    def __init__(self):
        self.points = 5000
        self.x_values = [0]
        self.y_values = [0]

    def random_walk(self):
        while len(self.x_values) < self.points:
            x_step = choice([1,-1])
            x_index = choice([0,1,2,3])
            x_go = x_step * x_index

            y_step = choice([1, -1])
            y_index = choice([0, 1, 2, 3])
            y_go = y_step * y_index

            if x_go==0 and y_go==0:
                continue

            x_where = self.x_values[-1] + x_go
            y_where = self.y_values[-1] + y_go
            self.x_values.append(x_where)
            self.y_values.append(y_where)