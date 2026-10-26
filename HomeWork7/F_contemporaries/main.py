import sys
from datetime import date
from enum import IntEnum


class EventType(IntEnum):
    END = 0
    START = 1


def main(lines: list[str] | None = None) -> list[frozenset[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    persons = []
    for i in range(n):
        d_born, m_born, y_born, d_dead, m_dead, y_dead = map(int, lines[i+1].split())
        persons.append((d_born, m_born, y_born, d_dead, m_dead, y_dead))

    events = []
    for idx, person in enumerate(persons, 1):
        d_birth, m_birth, y_birth, d_death, m_death, y_death = person

        birth_dt = date(y_birth, m_birth, d_birth)
        death_dt = date(y_death, m_death, d_death)

        yo18_dt = _birthday(birth_dt, 18)
        yo80_dt = _birthday(birth_dt, 80)

        if death_dt <= yo18_dt:
            continue

        events.append((yo18_dt, EventType.START, idx))
        events.append((min(yo80_dt, death_dt), EventType.END, idx))
    events.sort()

    res = []
    contemporaries = set()
    for dt, event_type, idx in events:
        if event_type == EventType.START:
            contemporaries.add(idx)
        elif event_type == EventType.END:
            c = frozenset(contemporaries)
            if not any(c.issubset(r) for r in res):
                res.append(c)
            contemporaries.remove(idx)

    return res or [frozenset([0])]


def _birthday(dt: date, age: int) -> date:
    try:
        return date(dt.year + age, dt.month, dt.day)
    except ValueError:
        return date(dt.year + age, 3, 1)


if __name__ == "__main__":
    result = main()
    for answer in result:
        print(*answer)
