# src/Days/Day17.py

from src.Day import Day
from src.Puzzle import Puzzle

from copy import deepcopy

ACTIVE = '#'
INACTIVE = '.'


class Cube():
    def __init__(self,
                 x: int = 0,
                 y: int = 0,
                 z: int = 0, val: str = None) -> None:
        self.x, self.y, self.z = x, y, z
        self.val = val

    def get_neighbor_coordinates(self):
        neighbors = []

        count = 1
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                for z in range(self.z - 1, self.z + 2):
                    # print(count, x, y, z)
                    if x == self.x and y == self.y and z == self.z:
                        continue
                    else:
                        neighbors.append([x, y, z])

                    count = count + 1

        return neighbors

    def __repr__(self) -> str:
        return f"[X: {self.x}, Y: {self.y}, Z: {self.z}, Value: {self.val}]"


class Cube4Dimension():
    def __init__(self,
                 x: int = 0,
                 y: int = 0,
                 z: int = 0,
                 w: int = 0,
                 val: str = None) -> None:
        self.x, self.y, self.z, self.w = x, y, z, w
        self.val = val

    def get_neighbor_coordinates(self):
        neighbors = []

        count = 1
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                for z in range(self.z - 1, self.z + 2):
                    for w in range(self.w - 1, self.w + 2):

                        # print(count, x, y, z, w)
                        # skip itself.
                        if x == self.x and \
                                y == self.y and \
                                z == self.z and \
                                w == self.w:
                            continue
                        else:
                            neighbors.append([x, y, z, w])

                        count = count + 1

        # print(len(neighbors))
        return neighbors

    def __repr__(self) -> str:
        return f"[X: {self.x}, Y: {self.y}, Z: {self.z}, Value: {self.val}]"


class Matrix():
    def __init__(self) -> None:
        self.cubes = {}
        self.depth = 0

    def build_matrix_cubes(self, lines: str = None, z: int = 0) -> dict:
        max_length = len(lines[0])
        MAX_SIZE = max_length * 2

        # Init a super large cube with all inactive.
        print("Initializing a super large cube")
        for x in range(-1 * MAX_SIZE, MAX_SIZE + 1):
            if x not in self.cubes:
                self.cubes[x] = {}

            for y in range(-1 * MAX_SIZE, MAX_SIZE + 1):
                if y not in self.cubes[x]:
                    self.cubes[x][y] = {}

                for z in range(-1 * MAX_SIZE, MAX_SIZE + 1):
                    self.cubes[x][y][z] = Cube(x, y, z, INACTIVE)

        # then change the initial locations
        z = 0
        self.depth = 1
        for x in range(max_length):
            line_elements = list(lines[x])

            for y in range(max_length):
                self.cubes[x][y][z] = Cube(x, y, z, line_elements[y])

    def get_active_neighbors(self, curr_cube: Cube = None):
        neighbors = curr_cube.get_neighbor_coordinates()
        active_neighbors = []

        for neigbor_coor in neighbors:
            (n_x, n_y, n_z) = neigbor_coor

            # borders and edges.
            if n_x not in self.cubes or \
                    n_y not in self.cubes[n_x] or \
                    n_z not in self.cubes[n_x][n_y]:
                continue

            if self.cubes[n_x][n_y][n_z].val == ACTIVE:
                active_neighbors.append(neigbor_coor)

        return active_neighbors

    def run_cycle(self):
        tmp_cubes = deepcopy(self.cubes)

        for x in self.cubes:
            for y in self.cubes[x]:
                for z in self.cubes[x][y]:
                    curr_cube = self.cubes[x][y][z]

                    active_neighbors = self.get_active_neighbors(curr_cube)
                    # print("CURR CUBE", curr_cube)
                    # print(len(active_neighbors))

                    if curr_cube.val == ACTIVE:          # active (#)
                        # If a cube is active and exactly 2 or 3 of its
                        # neighbors are also active, the cube remains active.
                        # Otherwise, the cube becomes inactive.
                        if len(active_neighbors) == 2 or \
                                len(active_neighbors) == 3:
                            tmp_cubes[x][y][z] = Cube(x, y, z, ACTIVE)
                        else:
                            tmp_cubes[x][y][z] = Cube(x, y, z, INACTIVE)

                    elif curr_cube.val == INACTIVE:      # inactive (.)
                        # If a cube is inactive but exactly 3 of its neighbors
                        # are active, the cube becomes active.
                        # Otherwise, the cube remains inactive.
                        if len(active_neighbors) == 3:
                            tmp_cubes[x][y][z] = Cube(x, y, z, ACTIVE)
                        else:
                            tmp_cubes[x][y][z] = Cube(x, y, z, INACTIVE)

        self.cubes = tmp_cubes

    def get_active_cubes(self):
        active_cubes = []
        for x in self.cubes:
            for y in self.cubes[x]:
                for z in self.cubes[x][y]:
                    curr_cube = self.cubes[x][y][z]

                    if curr_cube.val == ACTIVE:
                        active_cubes.append(curr_cube)

        return active_cubes

    def __repr__(self) -> str:
        ret = ""
        for z in range(-1 * self.depth, self.depth + 1):
            ret = f"{ret}\nZ: {z}"
            for x in self.cubes:
                row_vals = []

                for y in self.cubes[x]:
                    row_vals.append(self.cubes[x][y][z].val)

                ret = f"{ret}\n{''.join(row_vals)}"
            ret = f"{ret}\n"
        return ret


class Matrix4Dimension():
    def __init__(self) -> None:
        self.cubes = {}
        self.depth = 0

    def build_matrix_cubes(self, lines: str = None) -> dict:
        max_length = len(lines[0])
        MAX_SIZE = max_length * 2

        # Init a super large cube with all inactive.
        print("Initializing a super large cube")
        for x in range(-1 * MAX_SIZE, MAX_SIZE + 1):
            if x not in self.cubes:
                self.cubes[x] = {}

            for y in range(-1 * MAX_SIZE, MAX_SIZE + 1):
                if y not in self.cubes[x]:
                    self.cubes[x][y] = {}

                for z in range(-1 * MAX_SIZE, MAX_SIZE + 1):
                    if z not in self.cubes[x][y]:
                        self.cubes[x][y][z] = {}

                    for w in range(-1 * MAX_SIZE, MAX_SIZE + 1):
                        self.cubes[x][y][z][w] = Cube4Dimension(x, y, z, w, INACTIVE)

        # then change the initial locations
        z = 0
        w = 0
        self.depth = 1
        for x in range(max_length):
            line_elements = list(lines[x])

            for y in range(max_length):
                self.cubes[x][y][z][w] = Cube4Dimension(x, y, z, w, line_elements[y])

    def get_active_neighbors(self, curr_cube: Cube = None):
        neighbors = curr_cube.get_neighbor_coordinates()
        active_neighbors = []

        for neigbor_coor in neighbors:
            (n_x, n_y, n_z, n_w) = neigbor_coor

            # borders and edges.
            if n_x not in self.cubes or \
                    n_y not in self.cubes[n_x] or \
                    n_z not in self.cubes[n_x][n_y] or \
                    n_w not in self.cubes[n_x][n_y][n_z]:
                continue

            if self.cubes[n_x][n_y][n_z][n_w].val == ACTIVE:
                active_neighbors.append(neigbor_coor)

        return active_neighbors

    def run_cycle(self):
        tmp_cubes = deepcopy(self.cubes)

        for x in self.cubes:
            for y in self.cubes[x]:
                for z in self.cubes[x][y]:
                    for w in self.cubes[x][y][z]:
                        curr_cube = self.cubes[x][y][z][w]

                        active_neighbors = self.get_active_neighbors(curr_cube)
                        # print("CURR CUBE", curr_cube)
                        # print(len(active_neighbors))

                        if curr_cube.val == ACTIVE:          # active (#)
                            # If a cube is active and exactly 2 or 3 of its
                            # neighbors are also active, the cube remains active.
                            # Otherwise, the cube becomes inactive.
                            if len(active_neighbors) == 2 or \
                                    len(active_neighbors) == 3:
                                tmp_cubes[x][y][z][w] = Cube4Dimension(x, y, z, w, ACTIVE)
                            else:
                                tmp_cubes[x][y][z][w] = Cube4Dimension(x, y, z, w, INACTIVE)

                        elif curr_cube.val == INACTIVE:      # inactive (.)
                            # If a cube is inactive but exactly 3 of its neighbors
                            # are active, the cube becomes active.
                            # Otherwise, the cube remains inactive.
                            if len(active_neighbors) == 3:
                                tmp_cubes[x][y][z][w] = Cube4Dimension(x, y, z, w, ACTIVE)
                            else:
                                tmp_cubes[x][y][z][w] = Cube4Dimension(x, y, z, w, INACTIVE)

        self.cubes = tmp_cubes

    def get_active_cubes(self):
        active_cubes = []
        for x in self.cubes:
            for y in self.cubes[x]:
                for z in self.cubes[x][y]:
                    for w in self.cubes[x][y][z]:
                        curr_cube = self.cubes[x][y][z][w]

                        if curr_cube.val == ACTIVE:
                            active_cubes.append(curr_cube)

        return active_cubes



class Day17Puzzle1(Puzzle):
    """
    Day17 Puzzle1 class
    """
    def solve(self):
        print("Day17 - Puzzle1")
        lines = self.input.splitlines()

        matrix = Matrix()
        matrix.build_matrix_cubes(lines=lines, z=1)

        cycle_no = 1
        while(cycle_no <= 6):
            print(f"cycle no: {cycle_no}")

            matrix.run_cycle()
            print(matrix)

            cycle_no = cycle_no + 1

        result = len(matrix.get_active_cubes())

        print(f"Solution for Day17 Puzzle2: {result}")


class Day17Puzzle2(Puzzle):
    """
    Day17 Puzzle2 class
    """
    def solve(self):
        print("Day17 - Puzzle2")
        lines = self.input.splitlines()

        matrix = Matrix4Dimension()
        matrix.build_matrix_cubes(lines=lines)

        cycle_no = 1
        while(cycle_no <= 6):
            print(f"cycle no: {cycle_no}")

            matrix.run_cycle()
            # print(matrix)

            cycle_no = cycle_no + 1

        result = len(matrix.get_active_cubes())

        print(f"Solution for Day17 Puzzle2: {result}")


class Day17(Day):
    """
    Day17 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day17, self).__init__(day_number=17)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day17Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day17Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day17.day {}>".format(self.day_number)
