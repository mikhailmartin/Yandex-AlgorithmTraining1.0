import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    mountain_chain = [tuple(map(int, lines[1+i].split())) for i in range(n)]
    m = int(lines[1+n])
    tracks = [tuple(map(int, lines[1+n+1+i].split())) for i in range(m)]

    # 0-ий индекс - технический
    # 1-ый индекс - всегда 0
    prefix_sum_forward = [0] * (n+1)
    for i in range(2, n+1):
        ascent = max(mountain_chain[i-1][1] - mountain_chain[i-2][1], 0)
        prefix_sum_forward[i] = prefix_sum_forward[i-1] + ascent

    prefix_sum_backward = [0] * (n+2)
    for i in range(n-1, 0, -1):
        ascent = max(mountain_chain[i-1][1] - mountain_chain[i][1], 0)
        prefix_sum_backward[i] = prefix_sum_backward[i+1] + ascent

    results = []
    for start, finish in tracks:

        if start == finish:
            answer = 0
        elif start < finish:
            answer = prefix_sum_forward[finish] - prefix_sum_forward[start]
        elif start > finish:
            answer = prefix_sum_backward[finish] - prefix_sum_backward[start]

        results.append(answer)

    return results


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
