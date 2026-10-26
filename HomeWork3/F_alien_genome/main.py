import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    first_genome = lines[0]
    second_genome = lines[1]

    first_pairs = [first_genome[i:i+2] for i in range(len(first_genome)-1)]
    second_pairs = [second_genome[i:i + 2] for i in range(len(second_genome) - 1)]

    second_unique_pairs = set(second_pairs)

    proximity = 0
    for pair in first_pairs:
        if pair in second_unique_pairs:
            proximity += 1

    return proximity


if __name__ == "__main__":
    result = main()
    print(result)
