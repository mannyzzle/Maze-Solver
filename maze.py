import random
import time
from cell import Cell


class Maze:
    """
    2-D grid of Cell objects.  Handles maze carving *and* solving with DFS.
    """

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        # geometry & window
        self.__x1, self.__y1 = x1, y1
        self.__num_rows, self.__num_cols = num_rows, num_cols
        self.__cell_size_x, self.__cell_size_y = cell_size_x, cell_size_y
        self.__win = win

        if seed is not None:
            random.seed(seed)

        # grid creation
        self.__cells: list[list[Cell]] = []
        self.__create_cells()

        # carve, reset, ready to solve
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    # ============================================================ #
    # Grid creation / drawing                                      #
    # ============================================================ #
    def __create_cells(self):
        for col in range(self.__num_cols):
            self.__cells.append([Cell(self.__win) for _ in range(self.__num_rows)])

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    # ============================================================ #
    # Carving                                                      #
    # ============================================================ #
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        i_last = self.__num_cols - 1
        j_last = self.__num_rows - 1
        self.__cells[i_last][j_last].has_bottom_wall = False
        self.__draw_cell(i_last, j_last)

    def __break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True

        while True:
            neighbours = []

            # north
            if j > 0 and not self.__cells[i][j - 1].visited:
                neighbours.append(("N", i, j - 1))
            # south
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                neighbours.append(("S", i, j + 1))
            # west
            if i > 0 and not self.__cells[i - 1][j].visited:
                neighbours.append(("W", i - 1, j))
            # east
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                neighbours.append(("E", i + 1, j))

            if not neighbours:
                self.__draw_cell(i, j)
                return

            direction, ni, nj = random.choice(neighbours)
            neighbour = self.__cells[ni][nj]

            if direction == "N":
                current.has_top_wall = False
                neighbour.has_bottom_wall = False
            elif direction == "S":
                current.has_bottom_wall = False
                neighbour.has_top_wall = False
            elif direction == "W":
                current.has_left_wall = False
                neighbour.has_right_wall = False
            elif direction == "E":
                current.has_right_wall = False
                neighbour.has_left_wall = False

            self.__draw_cell(i, j)
            self.__draw_cell(ni, nj)
            self.__break_walls_r(ni, nj)

    # ============================================================ #
    # Solver                                                       #
    # ============================================================ #
    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        """Public entry—returns True if a path is found, else False."""
        self.__reset_cells_visited()
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        """Recursive DFS path-finder.  Returns True if end reached."""
        self.animate()
        current = self.__cells[i][j]
        current.visited = True

        # goal reached?
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        directions = [
            ("N",  i,     j - 1, current.has_top_wall,    lambda c, n: c.draw_move(n)),
            ("S",  i,     j + 1, current.has_bottom_wall, lambda c, n: c.draw_move(n)),
            ("W",  i - 1, j,     current.has_left_wall,   lambda c, n: c.draw_move(n)),
            ("E",  i + 1, j,     current.has_right_wall,  lambda c, n: c.draw_move(n)),
        ]

        for label, ni, nj, wall_present, draw_fn in directions:
            if (
                0 <= ni < self.__num_cols
                and 0 <= nj < self.__num_rows
                and not wall_present
                and not self.__cells[ni][nj].visited
            ):
                # forward move
                current.draw_move(self.__cells[ni][nj])
                if self.__solve_r(ni, nj):  # success propagates True up the stack
                    return True
                # back-track
                self.__cells[ni][nj].draw_move(current, undo=True)

        return False

    # ============================================================ #
    # Animation helper                                             #
    # ============================================================ #
    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.01)  # quick but visible


    # public accessor for tests
    def _get_cells_matrix(self):
        return self.__cells
