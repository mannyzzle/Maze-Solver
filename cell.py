from point import Point
from line import Line


class Cell:
    """A single maze cell with four potential walls."""

    def __init__(self, win=None):
        # wall state
        self.has_left_wall   = True
        self.has_right_wall  = True
        self.has_top_wall    = True
        self.has_bottom_wall = True

        # traversal bookkeeping
        self.visited = False

        # geometry – filled by draw()
        self.__x1 = self.__y1 = self.__x2 = self.__y2 = -1
        self.__win = win  # may be None for unit tests

    # ------------------------------------------------------------ #
    def draw(self, x1, y1, x2, y2):
        """Draw/erase four walls for this cell."""
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

        if self.__win is None:
            return

        bg = "white"  # default Tk background

        # left
        self.__win.draw_line(
            Line(Point(x1, y1), Point(x1, y2)),
            "black" if self.has_left_wall else bg,
        )
        # top
        self.__win.draw_line(
            Line(Point(x1, y1), Point(x2, y1)),
            "black" if self.has_top_wall else bg,
        )
        # right
        self.__win.draw_line(
            Line(Point(x2, y1), Point(x2, y2)),
            "black" if self.has_right_wall else bg,
        )
        # bottom
        self.__win.draw_line(
            Line(Point(x1, y2), Point(x2, y2)),
            "black" if self.has_bottom_wall else bg,
        )

    # ------------------------------------------------------------ #
    def draw_move(self, to_cell, undo=False):
        """Draw a red (forward) or gray (back-track) center-to-center line."""
        if self.__win is None:
            return

        color = "gray" if undo else "red"
        xm1 = (self.__x1 + self.__x2) / 2
        ym1 = (self.__y1 + self.__y2) / 2
        xm2 = (to_cell.__x1 + to_cell.__x2) / 2
        ym2 = (to_cell.__y1 + to_cell.__y2) / 2

        self.__win.draw_line(Line(Point(xm1, ym1), Point(xm2, ym2)), color)
