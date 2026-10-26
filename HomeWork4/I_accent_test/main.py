import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    dictionary = dict()
    for i in range(n):
        accent = lines[1+i]
        word = accent.lower()
        if word not in dictionary:
            dictionary[word] = [accent]
        else:
            dictionary[word].append(accent)
    test = lines[1+n]

    mistake_count = 0
    for accent in test.split():
        word = accent.lower()
        if word in dictionary:
            if accent not in dictionary[word]:
                mistake_count += 1
        else:
            if upper_count(accent) != 1:
                mistake_count += 1

    return mistake_count


def upper_count(accent):

    count = 0
    for char in accent:
        if char.isupper():
            count += 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
