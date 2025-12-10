type Vec2 = tuple[int, int]


def parse(data: str) -> list[Vec2]:
    return [(int(d.split(",")[0]), int(d.split(",")[1])) for d in data.splitlines()]


def area(a: Vec2, b: Vec2) -> int:
    return (1 + max(a[0], b[0]) - min(a[0], b[0])) * (1 + max(a[1], b[1]) - min(a[1], b[1]))


def a(data: str):
    tiles = parse(data)
    largest = 0
    for i, a in enumerate(tiles[:-1]):
        for b in tiles[i + 1 :]:
            largest = max(largest, area(a, b))

    return largest


def bounds(a: Vec2, b: Vec2):
    min_x, max_x = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
    min_y, max_y = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])

    return (min_x, min_y), (max_x, max_y)


def ranges_overlap(r1: Vec2, r2: Vec2) -> bool:
    return r1[0] < r2[1] and r1[1] > r2[0]


def any_overlap(range: Vec2, edges: list[Vec2]) -> bool:
    return any(ranges_overlap(range, v) for v in edges)


def point_in_polygon(p: Vec2, v_edges: dict[int, list[Vec2]]) -> bool:
    # count how many edges we cross to the east.
    # an odd number means we're inside
    # an even number means we're outside

    n = 0

    x, y = p

    for e_x in v_edges:
        if e_x < x:
            continue

        if any_overlap((y, y), v_edges[e_x]):
            n += 1
            continue

    return n % 2 == 1


def b(data: str):
    tiles = parse(data)
    n = len(tiles)

    h_edges: dict[int, list[Vec2]] = {}
    v_edges: dict[int, list[Vec2]] = {}

    for i in range(n):
        a, b = bounds(tiles[i], tiles[(i + 1) % n])

        (lo_x, lo_y), (hi_x, hi_y) = a, b

        if lo_x == hi_x:  # vertical
            v_edges.setdefault(lo_x, []).append((lo_y, hi_y))
        else:  # horizontal
            h_edges.setdefault(lo_y, []).append((lo_x, hi_x))

    largest = 0

    for i, a in enumerate(tiles[:-1]):
        for b in tiles[i + 1 :]:
            (lo_x, lo_y), (hi_x, hi_y) = bounds(a, b)

            h_e = [e for y in h_edges if lo_y < y < hi_y for e in h_edges[y]]
            v_e = [e for x in v_edges if lo_x < x < hi_x for e in v_edges[x]]

            # horizontal
            if any_overlap((lo_x, hi_x), h_e):
                continue

            # vertical
            if any_overlap((lo_y, hi_y), v_e):
                continue

            # still need to check that center is inside
            center = ((hi_x + lo_x) // 2, (hi_y + lo_y) // 2)
            if not point_in_polygon(center, v_edges):
                continue

            largest = max(largest, area(a, b))

    return largest
