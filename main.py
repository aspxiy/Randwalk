import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """定义随机游走的属性"""
    def __init__(self, points_num=5000):
        self.points_num = points_num

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.points_num:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_value = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_value = y_direction * y_distance

            x = self.x_values[-1] + x_value
            y = self.y_values[-1] + y_value

            self.x_values.append(x)
            self.y_values.append(y)


if __name__ == '__main__':
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()
