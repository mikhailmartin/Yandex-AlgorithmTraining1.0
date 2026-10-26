import sys


def main(lines: list[str] | None = None) -> int:
    """Подсмотрел решение на разборе задач. Тотально не понимаю условия"""
    lines = lines or sys.stdin.read().splitlines()

    k = int(lines[0])
    operations = lines[1]

    result = 0
    previous_length = 0
    for i in range(k, len(operations)):
        if operations[i] == operations[i - k]:
            previous_length += 1
            result += previous_length
        else:
            previous_length = 0

    return result


if __name__ == "__main__":
    result = main()
    print(result)
