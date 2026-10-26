import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    nums = []
    i = 0
    while True:
        num = int(lines[i])
        if num == -2_000_000_000:
            break
        else:
            nums.append(num)
            i += 1

    n = i
    if n in [0, 1]:
        return "RANDOM"

    is_asc = False
    is_desc = False
    is_const = False

    for j in range(1, n):

        prev = nums[j-1]
        curr = nums[j]

        if prev < curr:
            is_asc = True
        elif prev == curr:
            is_const = True
        else:
            is_desc = True

    if not is_asc and not is_desc and is_const:
        sequence_type = "CONSTANT"
    elif is_asc and not is_desc and not is_const:
        sequence_type = "ASCENDING"
    elif is_asc and not is_desc and is_const:
        sequence_type = "WEAKLY ASCENDING"
    elif not is_asc and is_desc and not is_const:
        sequence_type = "DESCENDING"
    elif not is_asc and is_desc and is_const:
        sequence_type = "WEAKLY DESCENDING"
    else:
        sequence_type = "RANDOM"

    return sequence_type


if __name__ == "__main__":
    result = main()
    print(result)
