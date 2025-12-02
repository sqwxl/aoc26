def sign(char):
    if char == "L":
        return -1
    if char == "R":
        return 1

    raise


def a(data: str):
    index = 50  # start position
    limit = 100
    count = 0

    for line in data.splitlines():
        index += sign(line[0]) * int(line[1:])

        index %= limit

        if index == 0:
            count += 1

    return count


def b(data: str):
    index = 50  # start position
    limit = 100
    count = 0

    for line in data.splitlines():
        index += sign(line[0]) * int(line[1:])

        count += abs(index // limit)

        index %= limit

    return count
