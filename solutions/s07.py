def parse(data: str):
    lines = data.splitlines()

    start_x = lines[0].index("S")

    manifold = [{j for j, c in enumerate(line) if c == "^"} for line in lines[1:]]

    return start_x, manifold


def a(data: str):
    start_x, manifold = parse(data)

    beams = {start_x}

    count = 0

    for splitters in manifold:
        if not splitters:
            continue

        hits = beams & splitters

        count += len(hits)

        splits = {x for h in hits for x in (h - 1, h + 1)}

        beams -= hits
        beams |= splits

    return count


def b(data: str):
    start_x, manifold = parse(data)

    beams = {start_x: 1}

    for splitters in manifold:
        if not splitters:
            continue

        hits = splitters & beams.keys()

        splits = {x: beams[x] for x in beams.keys() - hits}

        for h in hits:
            for x in (h - 1, h + 1):
                splits[x] = splits.get(x, 0) + beams[h]

        beams = splits

    return sum(beams.values())
