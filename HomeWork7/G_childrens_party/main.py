import sys
import bisect
from collections import deque
from enum import IntEnum


class EventType(IntEnum):
    READY = 0
    RESTED = 1


def main(lines: list[str] | None = None) -> tuple[int, list[int]]:

    lines = lines or sys.stdin.read().splitlines()

    m, n = map(int, lines[0].split())
    helpers = []
    for i in range(n):
        t, z, y = map(int, lines[i+1].split())
        helpers.append((t, z, y))

    if m == 0:
        return 0, [0] * n

    events = []
    for idx, (t, z, y) in enumerate(helpers):
        events.append((t, EventType.READY, idx))
    events.sort()
    events = deque(events)

    total = 0
    counter = [0] * n
    while events:
        time, event_type, idx = events.popleft()
        if event_type == EventType.READY:
            total += 1
            counter[idx] += 1

            if total == m:
                break

            t, z, y = helpers[idx]
            if counter[idx] % z == 0:
                bisect.insort(events, (time + y, EventType.RESTED, idx))
            else:
                bisect.insort(events, (time + t, EventType.READY, idx))

        elif event_type == EventType.RESTED:
            t, z, y = helpers[idx]
            bisect.insort(events, (time + t, EventType.READY, idx))

    return time, counter


if __name__ == "__main__":
    result = main()
    print(result[0])
    print(*result[1])
