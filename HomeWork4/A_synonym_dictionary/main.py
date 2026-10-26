import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])

    synonyms = dict()
    for i in range(n):
        word1, word2 = lines[1+i].split()
        synonyms[word1] = word2
        synonyms[word2] = word1

    word = lines[1+n].strip()

    return synonyms[word]


if __name__ == "__main__":
    result = main()
    print(result)
