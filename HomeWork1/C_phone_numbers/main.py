import sys


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    new_phone_number = normalized(lines[0])

    res = []
    for i in range(3):
        old_phone_number = normalized(lines[1+i])
        res.append("YES" if new_phone_number == old_phone_number else "NO")

    return res


def normalized(phone_number: str) -> str:

    phone_number = (
        phone_number
        .replace("+7", "8")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
    )

    if len(phone_number) == 11:
        phone_number = phone_number[1:]
    elif len(phone_number) == 7:
        phone_number = "495" + phone_number

    return phone_number


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
