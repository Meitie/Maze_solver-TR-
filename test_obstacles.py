import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot
import maze.obstacles as obstacles

class TestObstacles(unittest.TestCase):

    def test_is_position_blocked(self):
        obstacles.obstacles = [(2,2), (10,10)]
        self.assertTrue(obstacles.is_position_blocked(4, 4))
        self.assertFalse(obstacles.is_position_blocked(7, 4))
        self.assertFalse(obstacles.is_position_blocked(12, 4))
        self.assertTrue(obstacles.is_position_blocked(12, 12))
        self.assertFalse(obstacles.is_position_blocked(100, 16))
        self.assertFalse(obstacles.is_position_blocked(-35, -12))


    def test_is_path_blocked(self):
        obstacles.obstacles = [(2,2), (10,10)]
        self.assertTrue(obstacles.is_path_blocked(-10, 4, 10, 4))
        self.assertTrue(obstacles.is_path_blocked(5, 10, 5, -10))
        self.assertFalse(obstacles.is_path_blocked(-100,-20,-30,-20))


    def test_is_path_blocked_v2(self):
        obstacles.obstacles = [(0, -149)]
        self.assertTrue(obstacles.is_path_blocked(0, 0, 0, -150))
        self.assertTrue(obstacles.is_path_blocked(19, -148, -10, -148))


    def test_obst(self):
        obstacles.random.randint = lambda a, b: 1
        self.assertEqual([(1, 1)], obstacles.create_obstacles(-100, -200, 100, 200))


if __name__ == '__main__':
    unittest.main()