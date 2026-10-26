import sys


def main(lines: list[str] | None = None) -> int:
    """Находит самое высокое место, которое мог занять Тракторист Василий"""
    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    results = list(map(int, lines[1].split()))

    left_winner_index = find_left_winner_index(results)

    best_Vasya_result = find_best_Vasya_result(results, left_winner_index)

    if best_Vasya_result != float("-inf"):
        place = 1
        for result in results:
            if result > best_Vasya_result:
                place += 1
    else:
        place = 0

    return place


def find_left_winner_index(results: list[int]) -> int:
    """Возвращает индекс левого победителя"""
    winner_index = 0
    winner_result = results[winner_index]

    for index, result in enumerate(results):
        if result > winner_result:
            winner_index = index
            winner_result = result

    return winner_index


def find_best_Vasya_result(results: list[int], left_winner_index: int) -> int | float:
    """Находит лучший результат, удовлетворяющий условиям"""
    best_Vasya_result = float("-inf")

    # Если результат Василия был после победителя, и после результата Василия был ещё
    # результат поменьше, то индекс победителя должен быть максимум предпредпоследним
    # (третьим с конца).
    max_possible_winner_index = len(results) - 3
    if left_winner_index > max_possible_winner_index:
        return best_Vasya_result

    # Можно перебирать кандидатов от левого победителя до предпоследнего результата
    for i in range(left_winner_index+1, len(results) - 1):

        current_result = results[i]
        next_result = results[i+1]

        if (
            (current_result % 10) == 5
            and current_result > next_result
            and current_result > best_Vasya_result
        ):
            best_Vasya_result = current_result

    return best_Vasya_result


if __name__ == "__main__":
    place = main()
    print(place)
