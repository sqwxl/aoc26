def parse(data: str) -> list[tuple[str, str]]:
    return [
        (left, right)
        for d in data.strip().split(",")
        for (
            left,
            right,
        ) in [d.split("-", maxsplit=1)]
    ]


def has_repeats(s: str, divisor: int):
    length = len(s)

    if length % divisor > 0:
        return False

    size = length // divisor

    return s == s[:size] * divisor


def divisors(n: int) -> list[int]:
    f = []

    if n < 2:
        return f

    m = 2

    lim = n

    while m <= lim:
        if n % m == 0:
            f.append(m)
        m += 1

    return f


DIVISORS = {i: divisors(i) for i in range(1, 11)}


def a(data: str):
    ranges = parse(data)
    tally = 0

    for left, right in ranges:
        # skip odd length ID bounds that don't contain even IDs
        if len(left) % 2 != 0 and len(left) == len(right):
            continue

        lo, hi = int(left), int(right)

        for n in range(lo, hi + 1):
            if has_repeats(str(n), 2):
                tally += n

    return tally


def b(data: str):
    ranges = parse(data)

    hits = set()

    for left, right in ranges:
        lo, hi = int(left), int(right)

        for n in range(lo, hi + 1):
            s = str(n)

            for d in DIVISORS[len(s)]:
                if has_repeats(s, d):
                    hits.add(n)
                    break

    return sum(hits)
