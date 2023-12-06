from collections import defaultdict


class Point:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def delta(self, x=0, y=0):
        return Point(self.x + x, self.y + y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f"{self.x},{self.y}")

    def __repr__(self):
        return f"Vector({self.x},{self.y})"


def get_limits(point_sequence)->tuple:
    return (
        min([i.x for i in point_sequence]),
        max([i.x for i in point_sequence]),
        min([i.y for i in point_sequence]),
        max([i.y for i in point_sequence]),
    )


def get_map(path:str, start:Point)->defaultdict:
    the_map = defaultdict(lambda: '.')
    the_map[start] = '.'

    for l in open(path).readlines():
        l = l.strip()
        points = [[int(y) for y in x.split(',')] for x in l.split(' -> ')]

        for start, end in zip(points[:-1], points[1:]):
            xmin, xmax, ymin, ymax = get_limits((Point(*start), Point(*end)))

            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    the_map[Point(x, y)] = '#'

    return the_map


def visualize(the_map:defaultdict)->None:
    xmin, xmax, ymin, ymax = get_limits(the_map.keys())

    for y in range(ymin, ymax + 1):
        row = []
        for x in range(xmin, xmax + 1):
            row.append(the_map[Point(x, y)])

        print(*row, sep='')


def add_sand_block(the_map:defaultdict, start:Point, max_depth:int=0)->bool:
    if start.y >= max_depth:
        the_map[start] = '#'
        return False

    for c in (0, -1, 1):
        target = start.delta(x=c, y=1)
        if the_map[target] == '.':
            return add_sand_block(the_map, target, max_depth)

    the_map[start] = 'O'
    return True


def part1(path:str, do_visualize:bool):
    start = Point(500, 0)
    the_map = get_map(path, start)
    ymax = get_limits(the_map)[-1]
    while add_sand_block(the_map, start, ymax):
        pass

    if do_visualize:
        visualize(the_map)

    print(count_sand(the_map))


def count_sand(the_map:defaultdict)->int:
    return len([i for i in the_map.values() if i == 'O'])


def part2(path:str, do_visualize:bool):
    start = Point(500, 0)
    the_map = get_map(path, start)
    ymax = get_limits(the_map)[-1]
    while the_map[start] == '.':
        add_sand_block(the_map, start, ymax + 2)

    if do_visualize:
        visualize(the_map)
    print(count_sand(the_map))


if __name__ == '__main__':
    part1('sample.txt', False),
    part1('input.txt', False)
    part2('sample.txt', True),
    part2('input.txt', False),