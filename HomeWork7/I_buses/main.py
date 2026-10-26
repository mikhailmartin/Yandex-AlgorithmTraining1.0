import sys
from enum import IntEnum


class EventType(IntEnum):
    IN = 0
    OUT = 1


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    routes = []
    for i in range(m):
        f, x, g, y = lines[i+1].split()
        routes.append((f, x, g, y))

    events = []
    midnight_count = 0
    for src, time_out, dst, time_in in routes:
        src, dst = int(src), int(dst)
        time_out = convert(time_out)
        time_in = convert(time_in)

        events.append((time_out, EventType.OUT, src))
        events.append((time_in, EventType.IN, dst))

        if time_in < time_out:
            midnight_count += 1
    events.sort()

    # моделируем первые сутки
    bus_counter = [0] * (n + 1)
    balance = [0] * (n + 1)
    for time, event_type, city in events:
        if event_type == EventType.IN:
            bus_counter[city] += 1
            balance[city] += 1
        elif event_type == EventType.OUT:
            if bus_counter[city] > 0:
                bus_counter[city] -= 1
            balance[city] -= 1

    if any(count != 0 for count in balance):
        return -1

    # моделируем вторые сутки
    for time, event_type, city in events:
        if event_type == EventType.IN:
            bus_counter[city] += 1
        elif event_type == EventType.OUT:
            bus_counter[city] -= 1

    res = midnight_count
    for count in bus_counter:
        res += count

    return res


def convert(time: str) -> int:
    hh, mm = map(int, time.split(":"))
    return hh * 60 + mm


if __name__ == "__main__":
    result = main()
    print(result)
