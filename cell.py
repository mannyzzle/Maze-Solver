from point import Point
from line import Line

class Cell:
    def __init__(self, win=None):          # ✅ default to None
        self.has_left_wall   = True
        self.has_right_wall  = True
        self.has_top_wall    = True
        self.has_bottom_wall = True

        self.__x1 = self.__x2 = self.__y1 = self.__y2 = -1
        self.__win = win                   # may be None now

    # ------------------------------------------------------------
    def draw(self, x1, y1, x2, y2):
        self.__x1, self.__y1 = x1, y1
        self.__x2, self.__y2 = x2, y2

        if self.__win is None:             # ✅ headless mode
            return

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")

    # ------------------------------------------------------------
    def draw_move(self, to_cell, undo=False):
        if self.__win is None:             # ✅ headless mode
            return

        color = "gray" if undo else "red"

        xm1 = (self.__x1 + self.__x2) / 2
        ym1 = (self.__y1 + self.__y2) / 2
        xm2 = (to_cell.__x1 + to_cell.__x2) / 2
        ym2 = (to_cell.__y1 + to_cell.__y2) / 2

        self.__win.draw_line(Line(Point(xm1, ym1), Point(xm2, ym2)), color)
