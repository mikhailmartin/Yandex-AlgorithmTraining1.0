import sys
from enum import IntEnum


class EventType(IntEnum):
    CLOSE = 0
    OPEN = 1


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    offices = []
    for i in range(n):
        h_open, m_open, h_close, m_close = map(int, lines[i+1].split())
        offices.append((h_open, m_open, h_close, m_close))

    events = []
    for idx, (h_open, m_open, h_close, m_close) in enumerate(offices):
        time_open = h_open * 60 + m_open
        time_close = h_close * 60 + m_close
        if time_open < time_close:
            events.append((time_open, EventType.OPEN, idx))
            events.append((time_close, EventType.CLOSE, idx))
        else:
            events.append((time_open, EventType.OPEN, idx))
            events.append((24 * 60, EventType.CLOSE, idx))
            events.append((0, EventType.OPEN, idx))
            events.append((time_close, EventType.CLOSE, idx))
    events.sort()

    # первый проход
    opened = set()
    for time, event_type, idx in events:
        if event_type == EventType.OPEN:
            opened.add(idx)
        elif event_type == EventType.CLOSE:
            opened.discard(idx)

    # второй проход
    all_opened_time = 0
    for time, event_type, idx in events:
        if event_type == EventType.OPEN:
            opened.add(idx)
            if len(opened) == n:
                start = time
        elif event_type == EventType.CLOSE:
            if len(opened) == n:
                end = time
                all_opened_time += end - start
            opened.discard(idx)

    return all_opened_time


if __name__ == "__main__":
    result = main()
    print(result)
