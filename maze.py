import time
from cell import Cell

class Maze:
    def __init__(
        self,
        x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win=None            # 🆕 defaults to None
    ):
        self.__x1, self.__y1           = x1, y1
        self.__num_rows, self.__num_cols = num_rows, num_cols
        self.__cell_size_x, self.__cell_size_y = cell_size_x, cell_size_y
        self.__win = win

        self.__cells = []
        self.__create_cells()

    # ------------------------------------------------------------
    def __create_cells(self):
        for col in range(self.__num_cols):
            col_cells = [Cell(self.__win) for _ in range(self.__num_rows)]
            self.__cells.append(col_cells)

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    # ------------------------------------------------------------
    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    # ------------------------------------------------------------
    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    # small helper so tests / algorithms can reach cells
    def _get_cells_matrix(self):
        return self.__cells
