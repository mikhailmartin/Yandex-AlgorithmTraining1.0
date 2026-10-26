import sys


class Rectangle:
    def __init__(self, x: int, y: int):
        self.min_x_plus_y = x + y
        self.max_x_plus_y = x + y
        self.min_x_minus_y = x - y
        self.max_x_minus_y = x - y

    def increase(self, n_steps: int):
        self.min_x_plus_y -= n_steps
        self.max_x_plus_y += n_steps
        self.min_x_minus_y -= n_steps
        self.max_x_minus_y += n_steps

    def intersection(self, right):
        self.min_x_plus_y = max(self.min_x_plus_y, right.min_x_plus_y)
        self.max_x_plus_y = min(self.max_x_plus_y, right.max_x_plus_y)
        self.min_x_minus_y = max(self.min_x_minus_y, right.min_x_minus_y)
        self.max_x_minus_y = min(self.max_x_minus_y, right.max_x_minus_y)

    def get_points(self) -> list[tuple[int, int]]:

        points = []
        for x_plus_y in range(self.min_x_plus_y, self.max_x_plus_y+1):
            for x_minus_y in range(self.min_x_minus_y, self.max_x_minus_y+1):

                x, residual = divmod(x_plus_y + x_minus_y, 2)
                if residual == 0:
                    y = x_plus_y - x
                    point = (x, y)
                    points.append(point)

        return points


def main(lines: list[str] | None = None) -> list[tuple[int, int]]:

    lines = lines or sys.stdin.read().splitlines()

    t, d, n = map(int, lines[0].split())

    possible_rectangle = Rectangle(0, 0)
    for i in range(n):
        x, y = map(int, lines[1+i].split())
        possible_rectangle.increase(n_steps=t)
        navigator_rectangle = Rectangle(x, y)
        navigator_rectangle.increase(n_steps=d)
        possible_rectangle.intersection(navigator_rectangle)

    possible_points = possible_rectangle.get_points()

    return possible_points


if __name__ == "__main__":
    result = main()
    print(len(result))
    for possible_point in result:
        print(*possible_point)
