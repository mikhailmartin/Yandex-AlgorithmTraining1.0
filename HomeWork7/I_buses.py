"""
Автобусы

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Новый Президент Тридевятой республики начал свою деятельность с полной ревизии
системы общественного транспорта страны. В результате на основе социологических
опросов населения было составлено идеальное ежедневное расписание движения
междугородних автобусов, утвержденное Парламентом республики.

Более того, было решено заменить весь автобусный парк одинаковыми новыми, очень
дорогими, но гораздо более надёжными, красивыми и удобными машинами.

Автобусная сеть страны охватывает N городов, занумерованных целыми числами
от 1 до N.

Идеальное расписание содержит M ежедневных рейсов, i-й рейс начинается в
городе F_i в момент времени X_i и заканчивается в некотором другом городе G_i в
момент времени Y_i. Продолжительность каждого рейса ненулевая и строго меньше
24 часов. Рейс i выполняется одним из автобусов, находящихся в момент времени
X_i в городе F_i.

Новые автобусы не требуют ремонта и могут работать круглосуточно, поэтому
автобус, прибывший в некоторый момент времени в некоторый город, всегда готов
в тот же самый момент времени или позже отправиться в путь для обслуживания
любого другого рейса из данного города. Автобус может выехать из города, только
выполняя какой-либо рейс из расписания.

Предполагается, что расписание будет действовать неограниченное время, поэтому
может оказаться так, что его невозможно обслужить никаким конечным числом
автобусов.

Определите наименьшее количество новых автобусов, достаточное для обеспечения
движения по расписанию в течение неограниченного периода времени.


Формат ввода:
В первой строке задаются целые числа N и М (1 ≤ N, M ≤ 100 000) — количество
городов и рейсов автобусов соответственно.

В каждой из следующих M строк содержится описание рейса автобуса: номер города
отправления F_i, время отправления X_i, номер города назначения G_i (F_i ≠ G_i),
время прибытия Y_i, отделённые друг от друга одним пробелом. Время прибытия и
отправления задаётся в формате HH:MM, где HH — часы от 00 до 23, MM — минуты
от 00 до 59.


Формат ввода:
Выведите одно число — минимально необходимое количество автобусов. Если
расписание невозможно обслуживать в течение неограниченного периода времени
конечным числом автобусов, выведите число -1.


Пример 1
input: 2 2
input: 2 20:00 1 10:00
input: 1 08:00 2 21:00
output: 3

Пример 2
input: 2 2
input: 1 09:00 2 20:00
input: 2 20:00 1 09:00
output: 1

Пример 3
input: 3 4
input: 3 03:52 1 08:50
input: 1 18:28 3 21:53
input: 2 03:58 3 09:00
input: 3 14:59 2 21:13
output: 2
"""
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    IN = 0
    OUT = 1


@dataclass
class ProblemInput:
    n: int
    m: int
    routes: list[tuple[str, str, str, str]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, m = map(int, input().split())
        routes = []
        for _ in range(m):
            f, x, g, y = input().split()
            routes.append((f, x, g, y))
        return cls(ProblemInput(n, m, routes))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, m = map(int, lines[0].split())
        routes = []
        for i in range(m):
            f, x, g, y = lines[i+1].split()
            routes.append((f, x, g, y))
        return cls(ProblemInput(n, m, routes))

    def solve(self) -> int:

        events = []
        midnight_count = 0
        for src, time_out, dst, time_in in self.data.routes:
            src, dst = int(src), int(dst)
            time_out = self.convert(time_out)
            time_in = self.convert(time_in)

            events.append((time_out, EventType.OUT, src))
            events.append((time_in, EventType.IN, dst))

            if time_in < time_out:
                midnight_count += 1
        events.sort()

        # моделируем первые сутки
        bus_counter = [0] * (self.data.n + 1)
        balance = [0] * (self.data.n + 1)
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

        result = midnight_count
        for count in bus_counter:
            result += count

        return result

    @staticmethod
    def convert(time: str) -> int:
        hh, mm = map(int, time.split(":"))
        return hh * 60 + mm


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
