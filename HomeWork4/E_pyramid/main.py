import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    blocks = [tuple(map(int, lines[1+i].split())) for i in range(n)]

    some_dict = {}
    for width, height in blocks:
        if height > some_dict.get(width, 0):
            some_dict[width] = height

    height_pyramid = 0
    for width, height in some_dict.items():
        height_pyramid += height

    return height_pyramid


if __name__ == "__main__":
    result = main()
    print(result)
