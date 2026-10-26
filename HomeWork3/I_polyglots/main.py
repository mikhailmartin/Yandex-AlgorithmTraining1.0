if __name__ == "__main__":

    allknown_langs = set()
    all_langs = set()

    n = int(input())
    for i in range(n):
        m = int(input())
        current_langs = set()
        for _ in range(m):
            lang = input()
            current_langs.add(lang)
        all_langs |= current_langs
        if i == 0:
            allknown_langs = current_langs
        else:
            allknown_langs &= current_langs

    print(len(allknown_langs))
    print(*allknown_langs, sep="\n")
    print(len(all_langs))
    print(*all_langs, sep="\n")
