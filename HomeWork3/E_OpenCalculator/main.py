import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    present_buttons = set(lines[0].split())
    number = lines[1]

    required_buttons = set(number)
    lacking_buttons = required_buttons - present_buttons

    return len(lacking_buttons)


if __name__ == "__main__":
    n_lacking_numbers = main()
    print(n_lacking_numbers)
