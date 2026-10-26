import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    d = float(lines[3])
    e = float(lines[4])
    f = float(lines[5])

    if a == b == c == d == e == f == 0:
        return "5"
    elif a * d == b * c and a * f != c * e:
        return "0"
    elif a == 0 == b and e != 0:
        return "0"
    elif c == 0 == d and f != 0:
        return "0"
    elif a == 0 == c and b * f != d * e:
        return "0"
    elif b == 0 == d and a * f != c * e:
        return "0"
    elif a * d == b * c and a * f == c * e:
        if b == d == 0:
            if a != 0 and c != 0:
                return f"3 {e/a}"
            elif a == 0:
                if e == 0:
                    return f"3 {f/c}"
            elif c == 0:
                if f == 0:
                    return f"3 {e/a}"
        elif a == c == 0:
            if b != 0:
                return f"4 {e/b}"
            elif d != 0:
                return f"4 {f/d}"
        elif b != 0:
            return f"1 {-a/b} {e/b}"
        elif d != 0:
            return f"1 {-c/d} {f/d}"
    else:
        x = (e * d - b * f) / (a * d - b * c)
        y = (a * f - e * c) / (a * d - b * c)
        return f"2 {x} {y}"


if __name__ == "__main__":
    result = main()
    print(result)
