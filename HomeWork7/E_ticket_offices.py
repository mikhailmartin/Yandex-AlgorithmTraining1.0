"""
Кассы

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

На одном из московских вокзалов билеты продают N касс. Каждая касса работает без
перерыва определённый промежуток времени по фиксированному расписанию (одному и
тому же каждый день). Требуется определить, на протяжении какого времени
в течение суток работают все кассы одновременно.


Формат ввода:
Сначала вводится одно целое число N (0 < N ≤ 1000).

В каждой из следующих N строк через пробел расположены 4 целых числа, первые два
из которых обозначают время открытия кассы в часах и минутах (часы — целое число
от 0 до 23, минуты — целое число от 0 до 59), оставшиеся два — время закрытия
в том же формате. Числа разделены пробелами.

Время открытия означает, что в соответствующую ему минуту касса уже работает,
а время закрытия — что в соответствующую минуту касса уже не работает. Например,
касса, открытая с 10 ч. 30 мин. до 18 ч. 30 мин., ежесуточно работает 480 минут.

Если время открытия совпадает с временем закрытия, то касса работает
круглосуточно. Если первое время больше второго, то касса начинает работу до
полуночи, а заканчивает — на следующий день.


Формат вывода:
Требуется вывести одно число — суммарное время за сутки (в минутах),
на протяжении которого работают все N касс.


Пример 1
input: 3
input: 1 0 23 0
input: 12 0 12 0
input: 22 0 2 0
output: 120

Пример 2
input: 2
input: 9 30 14 0
input: 14 15 21 0
output: 0

Пример 3
input: 2
input: 14 00 18 00
input: 10 00 14 01
output: 1


Примечания:
1. Первая касса работает с часу до 23 часов, вторая – круглосуточно,
третья – с 22 часов до 2 часов ночи следующего дня. Таким образом, все три кассы
одновременно работают с 22 до 23 часов и с часу до двух часов, то есть 120 минут.
2. Первая касса работает до 14 часов, а вторая начинает работать в 14 часов
15 минут, то есть одновременно кассы не работают.
3. Вместе кассы работают лишь одну минуту – с 14:00 до 14:01 (в 14:01 вторая
касса уже не работает).
"""
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    CLOSE = 0
    OPEN = 1


@dataclass
class ProblemInput:
    n: int
    offices: list[tuple[int, int, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:

        n = int(input())
        offices = []
        for _ in range(n):
            h_open, m_open, h_close, m_close = map(int, input().split())
            offices.append((h_open, m_open, h_close, m_close))

        return cls(ProblemInput(n, offices))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n = int(lines[0])
        offices = []
        for i in range(n):
            h_open, m_open, h_close, m_close = map(int, lines[i+1].split())
            offices.append((h_open, m_open, h_close, m_close))

        return cls(ProblemInput(n, offices))

    def solve(self) -> int:

        events = []
        for idx, (h_open, m_open, h_close, m_close) in enumerate(self.data.offices):
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
                if len(opened) == self.data.n:
                    start = time
            elif event_type == EventType.CLOSE:
                if len(opened) == self.data.n:
                    end = time
                    all_opened_time += end - start
                opened.discard(idx)

        return all_opened_time


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
