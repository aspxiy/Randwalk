# A more intuitive and aesthetically pleasing version.(一個更直觀更美觀嘅版本)
import matplotlib.pyplot as plt
from random import choice


class RandomWalk:
    """定義隨機遊走嘅屬性(Define the properties of the random walk.)"""
    def __init__(self, points_num=10000):
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
    fig, ax = plt.subplots(figsize=(15, 9))                              # Fit to your screen.(適應屏幕)
    ax.scatter(rw.x_values, rw.y_values, s=15)
    points_numer = range(rw.points_num)
    ax.scatter(rw.x_values, rw.y_values, c=points_numer, 
               cmap=plt.cm.Blues, edgecolors='none', s=15)                # Use gradient colors to display the points. (使用漸變色來顯示點)
    ax.scatter(0, 0, c="green", edgecolors='none', s=100)                 # Highlight the starting point.(突出顯示起點)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)       # Highlight the ending point.(突出顯示終點)
    ax.get_xaxis().set_visible(False)                                     # Hide the X-axis.(隱藏x座標軸)
    ax.get_yaxis().set_visible(False)                                     # Hide the Y-axis.(隱藏y座標軸)
    plt.show()
