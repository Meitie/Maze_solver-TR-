import unittest
from io import StringIO
from unittest.mock import patch
import sys
import world.text.world as world

class TestRobot(unittest.TestCase):
    def test_move_forward(self):
        sys.stdout = StringIO()
        self.assertEqual((True, """ > Bob moved forward by 10 steps."""), world.do_forward("Bob", 10))
        self.assertEqual((True, """ > Bob moved forward by 100 steps."""), world.do_forward("Bob", 100))


    def test_co_ords_forward(self):
        sys.stdout = StringIO()
        world.position_x = 0
        world.position_y = 0
        self.assertEqual("allowed", world.update_position(80))
        self.assertEqual("allowed", world.update_position(1))
        self.assertEqual("allowed", world.update_position(0))
        self.assertEqual("outbounds", world.update_position(201))


    def test_move_backward(self):
        sys.stdout = StringIO()
        self.assertEqual((True, """ > Bob moved back by 10 steps."""), world.do_back("Bob", 10))
        self.assertEqual((True, """ > Bob moved back by 100 steps."""), world.do_back("Bob", 100))


    def test_turning_right(self):
        self.assertEqual((True, """ > HAL turned right."""), world.turn_right("HAL"))
        self.assertEqual((True, """ > BOB turned right."""), world.turn_right("BOB"))


    def test_turning_left(self):
        self.assertEqual((True, ' > HAL turned left.'),world.turn_left("HAL"))
        self.assertEqual((True, ' > Bob turned left.'),world.turn_left("Bob"))


    def test_out_of_bounds(self):
        self.assertTrue(world.is_position_allowed(80, 100))
        self.assertTrue(world.is_position_allowed(100, 200))
        self.assertTrue(world.is_position_allowed(0, 40))
        self.assertFalse(world.is_position_allowed(100, 300))


    def test_sprint_command(self):
        sys.stdout = StringIO()
        self.assertTrue(world.sprint("HAL", 5))
        self.assertTrue(world.sprint("HAL", 10))
        self.assertEqual(((True, 'HAL: Sorry, I cannot go outside my safe zone.')),world.sprint("HAL", 100))


if __name__ == '__main__':
    unittest.main()