import sys
from enum import IntEnum
from typing import Literal


class EventType(IntEnum):
    IN = 0
    OUT = 1


def main(lines: list[str] | None = None) -> list[Literal["Accepted", "Wrong Answer"]]:

    lines = lines or sys.stdin.read().splitlines()

    k = int(lines[0])
    res = []
    for j in range(k):
        test = list(map(int, lines[j+1].split()))
        n = test[0]
        guards = []
        for i in range(n):
            guards.append((test[1+i*2], test[1+i*2+1]))
        ans = _check(n, guards)
        res.append(ans)

    return res


def _check(n: int, guards: list[tuple[int, int]]) -> Literal["Accepted", "Wrong Answer"]:

    events = []
    for idx, (time_in, time_out) in enumerate(guards):
        events.append((time_in, EventType.IN, idx))
        events.append((time_out, EventType.OUT, idx))
    events.sort()

    good_seq = set()
    now_seq = set()
    good_flag = True
    prev_time = -1
    for time, event_type, idx in events:
        if time != 0 and len(now_seq) == 0:
            good_flag = False
            break

        if len(now_seq) == 1 and time != prev_time:
            good_seq.update(now_seq)

        if event_type == EventType.IN:
            now_seq.add(idx)
        elif event_type == EventType.OUT:
            now_seq.remove(idx)

        prev_time = time

    if events[-1][0] != 10000:
        good_flag = False

    if good_flag and len(good_seq) == n:
        return "Accepted"
    else:
        return "Wrong Answer"


if __name__ == "__main__":
    result = main()
    for answer in result:
        print(answer)
