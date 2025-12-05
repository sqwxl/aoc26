type Point = tuple[int, int]

OFFSETS = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]


def parse(data: str) -> set[Point]:
    cells = set()
    for i, row in enumerate(data.splitlines()):
        for j, c in enumerate(row):
            if c == "@":
                cells.add((i, j))

    return cells


def neighbors(cells: set[Point], p: Point) -> set[Point]:
    n = set()

    for di, dj in OFFSETS:
        q = (p[0] + di, p[1] + dj)
        if q in cells:
            n.add(q)

    return n


def is_available(cells: set[Point], p: Point) -> bool:
    count = 0
    for di, dj in OFFSETS:
        if (p[0] + di, p[1] + dj) in cells:
            count += 1
        if count >= 4:
            return False

    return True


def remove_available(cells: set[Point]) -> int:
    count = 0

    candidates = cells.copy()

    while candidates:
        to_remove = {c for c in candidates if is_available(cells, c)}

        if not to_remove:
            return count

        count += len(to_remove)

        cells -= to_remove

        candidates = set()
        for p in to_remove:
            candidates |= neighbors(cells, p)

    return count


def a(data: str):
    cells = parse(data)

    return len([p for p in cells if is_available(cells, p)])


def b(data: str):
    cells = parse(data)

    return remove_available(cells)
