import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    t_room, t_cond = map(int, lines[0].split())
    mode = lines[1]

    if mode == "freeze":
        t = t_cond if t_room >= t_cond else t_room
    elif mode == "heat":
        t = t_cond if t_cond >= t_room else t_room
    elif mode == "auto":
        t = t_cond
    elif mode == "fan":
        t = t_room
    else:
        assert False

    return t


if __name__ == "__main__":
    result = main()
    print(result)
