import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    x = int(lines[2])

    nearest_number = nums[0]
    nearest_dist = abs(x - nearest_number)

    for element in nums[1:]:

        current_dist = abs(x - element)

        if current_dist < nearest_dist:
            nearest_number = element
            nearest_dist = current_dist

    return nearest_number


if __name__ == "__main__":
    result = main()
    print(result)
