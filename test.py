import unittest
from maze import Maze

class Tests(unittest.TestCase):

    def test_maze_create_cells_12x10(self):
        cols, rows = 12, 10
        m = Maze(0, 0, rows, cols, 10, 10)   # win defaults to None
        self.assertEqual(len(m._Maze__cells), cols)
        self.assertEqual(len(m._Maze__cells[0]), rows)

    def test_maze_create_cells_3x3(self):
        cols, rows = 3, 3
        m = Maze(0, 0, rows, cols, 5, 5)
        self.assertEqual(len(m._Maze__cells), cols)
        self.assertEqual(len(m._Maze__cells[0]), rows)

    def test_maze_create_cells_1x5(self):
        cols, rows = 1, 5
        m = Maze(0, 0, rows, cols, 8, 8)
        self.assertEqual(len(m._Maze__cells), cols)
        self.assertEqual(len(m._Maze__cells[0]), rows)

if __name__ == "__main__":
    unittest.main()
