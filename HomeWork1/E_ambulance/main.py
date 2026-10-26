import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    k1, m, k2, p2, n2 = map(int, lines[0].split())

    entrance_number1 = -1
    floor_number1 = -1
    flag = False

    for flat_number in range(1, 1_000_000+1):  # количество квартир на этаже

        entrance, floor = validate(k1, m, k2, p2, n2, flat_number)

        if entrance != -1:
            flag = True
            if entrance_number1 == -1:
                entrance_number1, floor_number1 = entrance, floor
            elif entrance_number1 != entrance and entrance_number1 != 0:
                entrance_number1 = 0
            elif floor_number1 != floor and floor != 0:
                floor_number1 = 0

    if flag:
        return entrance_number1, floor_number1
    else:
        return -1, -1


def validate(
    k1: int, m: int, k2: int, p2: int, n2: int, flat_number: int
) -> tuple[int, int]:

    def get_entrance_and_floor(k: int, m: int, flat_number: int) -> tuple[int, int]:

        # номер лестничной площадки из всех площадок в доме
        landing_number = ((k - 1) // flat_number) + 1
        # номер подъезда
        entrance_number = ((landing_number - 1) // m) + 1
        # номер этажа
        floor_number = ((landing_number - 1) % m) + 1

        return entrance_number, floor_number

    entrance_number2, floor_number2 = get_entrance_and_floor(k2, m, flat_number)

    if p2 == entrance_number2 and n2 == floor_number2:
        entrance_number1, floor_number1 = get_entrance_and_floor(k1, m, flat_number)
    else:
        entrance_number1, floor_number1 = -1, -1

    return entrance_number1, floor_number1


if __name__ == "__main__":
    p1, n1 = main()
    print(p1, n1)
