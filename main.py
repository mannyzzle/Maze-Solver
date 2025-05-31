from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    Maze(50, 50, num_rows=10, num_cols=15, cell_size_x=40, cell_size_y=40, win=win)
    win.wait_for_close()

if __name__ == "__main__":
    main()
