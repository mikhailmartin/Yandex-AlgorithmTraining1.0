import sys
from enum import IntEnum


class EventType(IntEnum):
    BEGIN = 0
    POINT = 1
    END = 2


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    segments = []
    for i in range(n):
        a, b = map(int, lines[i+1].split())
        segments.append((a, b))
    points = list(map(int, lines[-1].split()))

    events = []
    for a, b in segments:
        begin, end = min(a, b), max(a, b)
        events.append((begin, EventType.BEGIN))
        events.append((end, EventType.END))
    for i, point in enumerate(points):
        events.append((point, EventType.POINT, i))
    events.sort()

    count = 0
    res = [0] * m
    for event in events:
        event_type = event[1]
        if event_type == EventType.BEGIN:
            count += 1
        elif event_type == EventType.POINT:
            i = event[2]
            res[i] = count
        elif event_type == EventType.END:
            count -= 1

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
