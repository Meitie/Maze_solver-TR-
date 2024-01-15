import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot
import maze_runner.solver as solve 

class TestMazes(unittest.TestCase):

    def test_solve_top(self):
        sys.stdout = StringIO()
        self.assertEqual((True, "Hal: I am at the top edge."), solve.maze_solver("Hal", "top"))
        self.assertEqual((True, "Hal: I am at the bottom edge."), solve.maze_solver("Hal", "bottom"))
        self.assertEqual((True, "Hal: I am at the left edge."), solve.maze_solver("Hal", "left"))
        self.assertEqual((True, "Hal: I am at the right edge."), solve.maze_solver("Hal", "right"))

if __name__ == '__main__':
    unittest.main()
