import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    powers = list(map(int, lines[1].split(" ")))
    m = int(lines[2])
    power_price = [tuple(map(int, lines[3+i].split(" "))) for i in range(m)]

    power_price = preprocessed(power_price)

    total_cost = 0
    for power in powers:
        for power_, price_ in power_price:
            if power_ < power:
                continue
            else:
                total_cost += price_
                break

    return total_cost


def preprocessed(old_power_price: list[tuple[int, int]]) -> list[tuple[int, int]]:

    old_power_price = sorted(old_power_price, reverse=True)
    for i in range(1, len(old_power_price)):
        current_power, current_price = old_power_price[i]
        previous_power, previous_price = old_power_price[i - 1]
        old_power_price[i] = (current_power, min(current_price, previous_price))

    old_power_price = sorted(old_power_price)
    new_power_price = [old_power_price[0]]
    previous_power = old_power_price[0][0]
    for power, price in old_power_price:
        if power != previous_power:
            new_power_price.append((power, price))
            previous_power = power

    return new_power_price


if __name__ == "__main__":
    result = main()
    print(result)
