import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    points = [tuple(map(int, lines[1+i].split())) for i in range(n)]

    res = 0
    for core_point in points:

        dists = []
        symmetrics = set()
        for other_point in points:
            dist = get_distance(core_point, other_point)
            dists.append(dist)

            # проверка на вырожденный треугольник
            if other_point in symmetrics:
                res -= 1

            symmetric = get_symmetric(other_point, core_point)
            symmetrics.add(symmetric)
        dists.sort()

        right = 0
        for left in range(len(dists)):
            while right < len(dists) and dists[left] == dists[right]:
                right += 1
            res += right - left - 1

    return res


def get_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def get_symmetric(point: tuple[int, int], center: tuple[int, int]) -> tuple[int, int]:
    dx = center[0] - point[0]
    dy = center[1] - point[1]
    return point[0] + 2 * dx, point[1] + 2 * dy


if __name__ == "__main__":
    result = main()
    print(result)
