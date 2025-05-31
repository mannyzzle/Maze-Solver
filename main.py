from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(700, 100)
    line1 = Line(p1, p2)
    win.draw_line(line1, "red")

    p3 = Point(100, 200)
    p4 = Point(700, 500)
    line2 = Line(p3, p4)
    win.draw_line(line2, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()
