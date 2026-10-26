import sys
from enum import IntEnum


class EventType(IntEnum):
    OUT = 0
    IN = 1


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, w, l = map(int, lines[0].split())
    blocks = []
    for i in range(n):
        x1, y1, z1, x2, y2, z2 = map(int, lines[i+1].split())
        blocks.append((x1, y1, z1, x2, y2, z2))

    events = []
    for i, (x1, y1, z1, x2, y2, z2) in enumerate(blocks, 1):
        area = (x2 - x1) * (y2 - y1)
        events.append((z1, EventType.IN, area, i))
        events.append((z2, EventType.OUT, area, i))
    events.sort()

    # за первый проход выясняем, существует ли решение
    total_area = w * l
    curr_area = 0
    success = False
    count = 0
    min_count = 10 ** 5 + 1
    for z, event_type, area, i in events:
        if event_type == EventType.IN:
            curr_area += area
            count += 1
            if curr_area == total_area:
                success = True
                min_count = min(min_count, count)
        elif event_type == EventType.OUT:
            curr_area -= area
            count -= 1

    if not success:
        return []

    # за второй проход ищем набор блоков
    curr_area = 0
    count = 0
    blocks = set()
    for z, event_type, area, i in events:
        if event_type == EventType.IN:
            curr_area += area
            count += 1
            blocks.add(i)
            if curr_area == total_area and count == min_count:
                break
        elif event_type == EventType.OUT:
            curr_area -= area
            count -= 1
            blocks.remove(i)

    return sorted(blocks)


if __name__ == "__main__":
    result = main()
    n = len(result)
    if n == 0:
        print("NO")
    else:
        print("YES")
        print(n)
        print("\n".join(map(str, result)))
