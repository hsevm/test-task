import getopt
import random
import sys
from typing import List


class Map:
    map2d: List[List[str]]
    robot_pos: (int, int)

    def size(self):
        return len(self.map2d)

    # generate a random map with passed size
    def __init__(self, n: int):
        self.map2d = [['.' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                self.map2d[i][j] = random.choice(['.', '#'])
        self.robot_pos = (random.randrange(n), random.randrange(n))
        self.map2d[self.robot_pos[0]][self.robot_pos[1]] = 'R'

    def __str__(self):
        return '\n'.join([' '.join(raw) for raw in self.map2d])

    def find_closest_obstacles(self):
        def find_closest_obstacle_in_dir(offset: (int, int)):
            raw, col = (self.robot_pos[0], self.robot_pos[1])
            while raw in range(self.size()) and col in range(self.size()) and self.map2d[raw][col] != '#':
                raw += offset[0]
                col += offset[1]
            return raw, col

        return {0: find_closest_obstacle_in_dir((-1, 0)),
                90: find_closest_obstacle_in_dir((0, 1)),
                180: find_closest_obstacle_in_dir((1, 0)),
                270: find_closest_obstacle_in_dir((0, -1))
                }


def main(argv):
    # default options
    n = 5
    s = 1

    try:
        opts, args = getopt.getopt(argv, "n:s:")
    except getopt.GetoptError:
        print("app.py [-n <map dimensions>] [-s <cell size>]")
        sys.exit()
    for opt, arg in opts:
        if opt == "-n":
            n = int(arg)
        elif opt == "-s":
            s = float(arg)

    map2d = Map(n)
    print("Map: n = {}, s = {}\n".format(n, s), map2d, sep='')
    print("Robot:", tuple(map(lambda a, b: (a + b) * s, (map2d.robot_pos[1], map2d.robot_pos[0]), (0.5, 0.5))))

    closest_obstacles = {k: (v[1], v[0]) for k, v in map2d.find_closest_obstacles().items()}
    offsets = {
        0: (0.5, 1),
        90: (0, 0.5),
        180: (0.5, 0),
        270: (1, 0.5)
    }
    print("Obstacles:",
          {k: tuple(map(lambda a, b: (a + b) * s, v, offsets[k])) for k, v in closest_obstacles.items()})


if __name__ == "__main__":
    main(sys.argv[1:])
