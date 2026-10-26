import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k, m = map(int, lines[0].split())

    component_num_total = 0
    material = n

    while True:
        blank_num_t, blank_residual_t = divmod(material, k)
        if not blank_num_t:
            break

        component_num, component_residual = divmod(k, m)
        if not component_num:
            break

        component_num_total += blank_num_t * component_num
        material = blank_residual_t + blank_num_t * component_residual

    return component_num_total


if __name__ == "__main__":
    component_num = main()
    print(component_num)
