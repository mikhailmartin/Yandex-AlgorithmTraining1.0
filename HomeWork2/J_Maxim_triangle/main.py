import sys


def main(lines: list[str] | None = None) -> tuple[float, float]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    first_freq = float(lines[1])
    freqs_answers = []
    for i in range(n-1):
        freq, answer = lines[2+i].split()
        freq = float(freq)
        freqs_answers.append((freq, answer))

    left_border = 30.0
    right_border = 4000.0
    prev_freq = first_freq
    for freq, answer in freqs_answers:
        if answer == "closer":
            if freq < prev_freq:
                right_border = min(right_border, (freq + prev_freq) / 2)
            elif freq > prev_freq:
                left_border = max(left_border, (freq + prev_freq) / 2)
        elif answer == "further":
            if freq < prev_freq:
                left_border = max(left_border, (freq + prev_freq) / 2)
            elif freq > prev_freq:
                right_border = min(right_border, (freq + prev_freq) / 2)
        prev_freq = freq

    return left_border, right_border


if __name__ == "__main__":
    left_border, right_border = main()
    print(left_border, right_border)
