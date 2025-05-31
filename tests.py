import unittest
from maze import Maze


class Tests(unittest.TestCase):

    # -------------------------------------------------------- #
    # Dimension checks                                         #
    # -------------------------------------------------------- #
    def test_maze_create_cells_12x10(self):
        m = Maze(0, 0, 10, 12, 10, 10, seed=0)
        self.assertEqual(len(m._Maze__cells), 12)
        self.assertEqual(len(m._Maze__cells[0]), 10)

    def test_maze_create_cells_3x3(self):
        m = Maze(0, 0, 3, 3, 5, 5, seed=0)
        self.assertEqual(len(m._Maze__cells), 3)
        self.assertEqual(len(m._Maze__cells[0]), 3)

    # -------------------------------------------------------- #
    # Entrance / exit walls                                    #
    # -------------------------------------------------------- #
    def test_break_entrance_and_exit(self):
        m = Maze(0, 0, 4, 4, 10, 10, seed=0)
        self.assertFalse(m._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m._Maze__cells[3][3].has_bottom_wall)

    # -------------------------------------------------------- #
    # 🆕 Visited reset check                                    #
    # -------------------------------------------------------- #
    def test_reset_cells_visited(self):
        m = Maze(0, 0, 5, 5, 10, 10, seed=0)
        for column in m._Maze__cells:
            for cell in column:
                self.assertFalse(cell.visited)


    def test_maze_solver(self):
        """Solver should return True for a carveable maze."""
        m = Maze(0, 0, 6, 6, 10, 10, seed=0)  # deterministic grid
        self.assertTrue(m.solve())            # must find a path
        # ensure goal cell is visited
        self.assertTrue(m._Maze__cells[5][5].visited)



if __name__ == "__main__":
    unittest.main()
