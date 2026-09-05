"""
Современники

Ограничение времени - 3 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Группа людей называется современниками, если был такой момент, когда они могли
собраться все вместе и обсуждать какой-нибудь важный вопрос. Для этого в тот
момент, когда они собрались, каждому из них должно было уже исполниться 18 лет,
но ещё не исполниться 80 лет.

Вам дан список великих людей с датами их жизни. Выведите всевозможные
максимальные множества современников. Множество современников будем называть
максимальным, если нет другого множества современников, которое включает в себя
всех людей из первого множества.

Будем считать, что в день своего 18-летия человек уже может принимать участие в
такого рода собраниях, а в день 80-летия, равно как и в день своей смерти, — нет.


Формат ввода:
Сначала на вход программы поступает число N — количество людей (1 ≤ N ≤ 10000).
Далее в N строках вводится по шесть чисел — первые три задают дату (день, месяц,
год) рождения, следующие три — дату смерти (она всегда не ранее даты рождения).
День (в зависимости от месяца, а в феврале — ещё и года) от 1 до 28, 29, 30 или
31, месяц — от 1 до 12, год — от 1 до 2005.


Формат вывода:
Программа должна вывести все максимальные множества современников. Каждое
множество должно быть записано на отдельной строке и содержать номера людей
(люди во входных данных нумеруются в порядке их задания, начиная с 1). Номера
людей должны разделяться пробелами.

Никакое множество не должно быть указано дважды.

Если нет ни одного непустого максимального множества, выведите одно число 0.

Гарантируется, что входные данные будут таковы, что размер выходных данных для
правильного ответа не превысит 2 Мб.


Пример 1
input: 3
input: 2 5 1988 13 11 2005
input: 1 1 1 1 1 30
input: 1 1 1910 1 1 1990
output: 2
output: 3

Пример 2
input: 3
input: 2 5 1968 13 11 2005
input: 1 1 1 1 1 30
input: 1 1 1910 1 1 1990
output: 2
output: 1 3

Пример 3
input: 3
input: 2 5 1988 13 11 2005
input: 1 1 1 1 1 10
input: 2 1 1910 1 1 1928
output: 0
"""
from dataclasses import dataclass
from datetime import date
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    END = 0
    START = 1


@dataclass
class ProblemInput:
    n: int
    persons: list[tuple[int, int, int, int, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:

        n = int(input())
        persons = []
        for _ in range(n):
            d_born, m_born, y_born,  d_dead, m_dead, y_dead = map(int, input().split())
            persons.append((d_born, m_born, y_born,  d_dead, m_dead, y_dead))

        return cls(ProblemInput(n, persons))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n = int(lines[0])
        persons = []
        for i in range(n):
            d_born, m_born, y_born, d_dead, m_dead, y_dead = map(int, lines[i+1].split())
            persons.append((d_born, m_born, y_born, d_dead, m_dead, y_dead))

        return cls(ProblemInput(n, persons))

    def solve(self) -> list[frozenset[int]]:

        events = self._build_events()

        result = []
        contemporaries = set()
        for dt, event_type, idx in events:
            if event_type == EventType.START:
                contemporaries.add(idx)
            elif event_type == EventType.END:
                c = frozenset(contemporaries)
                if not any(c.issubset(r) for r in result):
                    result.append(c)
                contemporaries.remove(idx)

        return result or [frozenset([0])]

    def _build_events(self) -> list[tuple[date, EventType, int]]:

        events = []
        for idx, person in enumerate(self.data.persons, 1):
            d_birth, m_birth, y_birth, d_death, m_death, y_death = person

            birth_dt = date(y_birth, m_birth, d_birth)
            death_dt = date(y_death, m_death, d_death)

            yo18_dt = self._birthday(birth_dt, 18)
            yo80_dt = self._birthday(birth_dt, 80)

            if death_dt <= yo18_dt:
                continue

            events.append((yo18_dt, EventType.START, idx))
            events.append((min(yo80_dt, death_dt), EventType.END, idx))
        events.sort()

        return events

    @staticmethod
    def _birthday(dt: date, age: int) -> date:
        try:
            return date(dt.year + age, dt.month, dt.day)
        except ValueError:
            return date(dt.year + age, 3, 1)


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(*answer)


if __name__ == "__main__":
    main()
