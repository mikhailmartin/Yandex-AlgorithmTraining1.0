import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))

    i_start_palindrome = 0
    i_sym = -1
    for i in range(len(nums)):
        if nums[i] != nums[i_sym]:
            i_start_palindrome = i + 1
            i_sym = -1  # сдвигаем индекс влево
        else:
            i_sym -= 1  # откатываем индекс на конец

    return list(reversed(nums[:i_start_palindrome]))


if __name__ == "__main__":
    result = main()
    print(len(result))
    print(" ".join(map(str, result)))
