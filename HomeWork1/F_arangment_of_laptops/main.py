import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    a1, b1, a2, b2 = map(int, lines[0].split())

    # разворачиваем ноутбуки, так что a - большая, b - меньшая сторона
    if b1 > a1:
        a1, b1 = b1, a1
    if b2 > a2:
        a2, b2 = b2, a2

    # упорядочиваем ноутбуки так, что 1 - побольше, 2 - поменьше
    if a2 > a1 or (a2 == a1 and b2 > b1):
        a1, b1, a2, b2 = a2, b2, a1, b1

    a3_1 = a1
    b3_1 = b1 + b2
    area_1 = a3_1 * b3_1

    a3_2 = a1 + b2
    b3_2 = max(b1, a2)
    area_2 = a3_2 * b3_2

    if area_1 < area_2:
        return a3_1, b3_1
    else:
        return a3_2, b3_2


if __name__ == "__main__":
    a3, b3 = main()
    print(a3, b3)
