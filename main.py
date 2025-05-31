from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    m = Maze(40, 40, 15, 20, 25, 25, win=win)  # random carve each run
    m.solve()                                  # watch the solver
    win.wait_for_close()

if __name__ == "__main__":
    main()
