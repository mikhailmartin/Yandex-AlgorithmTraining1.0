import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])
    d = int(lines[3])
    e = int(lines[4])

    # упорядочиваем размеры кирпича в порядке неубывания
    if a > b:
        a, b, c = b, a, c
    if b > c:
        a, b, c = a, c, b
    if a > b:
        a, b, c = b, a, c

    # упорядочимваем размеры отверстия
    if d > e:
        d, e = e, d

    # проверяем пролезет ли кирпич в дырку
    if a <= d and b <= e:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    result = main()
    print(result)
