import sys
from enum import IntEnum


class EventType(IntEnum):
    IN = 0
    START = 1
    END = 2
    OUT = 3


def main(lines: list[str] | None = None) -> tuple[int, int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    customers = []
    for i in range(n):
        time_in, time_out = map(int, lines[i+1].split())
        customers.append((time_in, time_out))
    promo = 5

    events = []
    seen = set()
    for i, (time_in, time_out) in enumerate(customers):
        if time_out - time_in >= promo:
            events.append((time_in, EventType.IN, i))
            events.append((time_out, EventType.OUT, i))

            time_start = time_in
            time_end = time_in + promo
            if time_start not in seen:
                events.append((time_start, EventType.START, i))
                events.append((time_end, EventType.END, i))
                seen.add(time_start)

            time_start = time_out - promo
            time_end = time_out
            if time_start not in seen:
                events.append((time_start, EventType.START, i))
                events.append((time_end, EventType.END, i))
                seen.add(time_start)
    events.sort()

    curr_active = 0
    start_active = dict()
    time_active: dict[int, int] = dict()
    for time, event_type, i in events:
        if event_type == EventType.OUT:
            curr_active &= ~(1 << i)
        elif event_type == EventType.IN:
            curr_active |= 1 << i
        elif event_type == EventType.START:
            start_active[time] = curr_active
        elif event_type == EventType.END:
            start_time = time - promo
            before_active = start_active[start_time]
            time_active[start_time] = before_active & curr_active
    del events

    time_active: list[tuple[int, int]] = list(time_active.items())
    n = len(time_active)

    max_customers = 0
    start1 = 1
    start2 = 1 + promo
    for i in range(n):
        time1, active1 = time_active[i]

        if active1.bit_count() > max_customers:
            max_customers = active1.bit_count()
            start1 = time1
            start2 = time1 + promo

        for j in range(i + 1, n):
            time2, active2 = time_active[j]

            if abs(time1 - time2) < promo:
                continue

            customers = active1 | active2
            if customers.bit_count() > max_customers:
                max_customers = customers.bit_count()
                start1 = time1
                start2 = time2

    return max_customers, *sorted([start1, start2])


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
