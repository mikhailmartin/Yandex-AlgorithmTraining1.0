import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    intervals = []
    for i in range(m):
        b, e = map(int, lines[i+1].split())
        intervals.append((b, e))

    events = []
    for begin, end in intervals:
        events.append((begin, 1))
        events.append((end + 1, -1))
    events.sort()

    supervised = 0
    supervisors = 0
    prev_pos = 0

    i = 0
    n_events = len(events)
    while i < n_events:
        curr_pos = events[i][0]

        if supervisors > 0:
            supervised += curr_pos - prev_pos

        while i < n_events and events[i][0] == curr_pos:
            supervisors += events[i][1]
            i += 1

        prev_pos = curr_pos

    return n - supervised


if __name__ == "__main__":
    result = main()
    print(result)
