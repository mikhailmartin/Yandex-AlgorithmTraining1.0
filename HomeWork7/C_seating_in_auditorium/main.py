import sys
from collections import deque
from enum import IntEnum


class EventType(IntEnum):
    BEGIN = 0
    END = 1


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, d = map(int, lines[0].split())
    students = list(map(int, lines[1].split()))

    events = []
    for i, student in enumerate(students):
        events.append((student, EventType.BEGIN, i))
        events.append((student + d, EventType.END, i))
    events.sort()

    available = deque()
    res = [0] * n
    next_variant = 1
    for _, event_type, i in events:
        if event_type == EventType.BEGIN:
            if not available:
                available.append(next_variant)
                next_variant += 1
            res[i] = available.popleft()
        elif event_type == EventType.END:
            available.append(res[i])

    return res


if __name__ == "__main__":
    result = main()
    print(max(result))
    print(" ".join(map(str, result)))
