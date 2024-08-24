"""
Пробежки по Манхэттену

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дороги Нью-Манхэттена устроены следующим образом. С юга на север через каждые
сто метров проходит авеню, с запада на восток через каждые сто метров проходит
улица. Авеню и улицы нумеруются целыми числами. Меньшие номера соответствуют
западным авеню и южным улицам. Таким образом, можно построить прямоугольную
систему координат так, чтобы точка (x, y) лежала на пересечении x-ой авеню и
y-ой улицы. Легко заметить, что для того, чтобы в Нью-Манхэттене дойти от точки
(x_1, y_1) до точки (x_2, y_2) нужно пройти |x_2 − x_1| + |y_2 − y_1| кварталов.
Эта величина называется манхэттенским расстоянием между точками (x_1, y_1) и
(x_2, y_2).

Миша живет в Нью-Манхэттене и каждое утро делает пробежку по городу. Он
выбегает из своего дома, который находится в точке (0, 0) и бежит по случайному
маршруту. Каждую минуту Миша либо остаётся на том же перекрестке, что и минуту
назад, или перемещается на один квартал в любом направлении. Чтобы не
заблудиться Миша берёт с собой навигатор, который каждые t минут говорит Мише,
в какой точке он находится. К сожалению, навигатор показывает не точное
положение Миши, он может показать любую из точек, манхэттенское расстояние от
которых до Миши не превышает d.

Через t × n минут от начала пробежки, получив n-е сообщение от навигатора, Миша
решил, что пора бежать домой. Для этого он хочет понять, в каких точках он
может находиться. Помогите Мише сделать это.


Формат ввода:
Первая строка входного файла содержит числа t, d и n (1 ≤ t ≤ 100, 1 ≤ d ≤ 100,
1 ≤ n ≤ 100).

Далее n строк описывают данные, полученные от навигатора. Строка номер i
содержит числа x_i и y_i — данные, полученные от навигатора через t_i минут от
начала пробежки.


Формат вывода:
В первой строке выходного файла выведите число m — число точек, в которых может
находиться Миша. Далее выведите m пар чисел — координаты точек. Точки можно
вывести в произвольном порядке.

Гарантируется, что навигатор исправен и что существует по крайней мере одна
точка, в которой может находиться Миша.


Пример 1
input: 2 1 5
input: 0 1
input: -2 1
input: -2 3
input: 0 3
input: 2 5
output: 2
output: 1 5
output: 2 4

Пример 2
input: 1 1 1
input: 0 0
output: 5
output: -1 0
output: 0 -1
output: 0 0
output: 0 1
output: 1 0

Пример 3
input: 1 10 1
input: 0 0
output: 5
output: -1 0
output: 0 -1
output: 0 0
output: 0 1
output: 1 0
"""


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


def main(
        t: int,
        d: int,
        navigator_points: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    """
    Возвращает список возможных точек, в которых может находиться Михаил.

    Parameters:
        t: количество минут через которые навигатор сообщает координаты.
        d: максимальная ошибка навигатора в манхеттенском расстоянии.
        navigator_points: список координат, которые сообщал навигатор.

    Returns:
        Список возможных точек, в которых может находиться Михаил.
    """
    possible_rectangle = Rectangle(0, 0)

    for x, y in navigator_points:
        possible_rectangle.increase(n_steps=t)
        navigator_rectangle = Rectangle(x, y)
        navigator_rectangle.increase(n_steps=d)
        possible_rectangle.intersection(navigator_rectangle)

    possible_points = possible_rectangle.get_points()

    return possible_points


if __name__ == "__main__":

    t, d, n = map(int, input().split())
    navigator_points = [tuple(map(int, input().split())) for _ in range(n)]
    possible_points = main(t, d, navigator_points)
    print(len(possible_points))
    for possible_point in possible_points:
        print(*possible_point)
