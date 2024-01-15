import unittest
from io import StringIO
from unittest.mock import patch
import sys
import robot


class TestRobot(unittest.TestCase):

    @patch("sys.stdin", StringIO("HAL"))
    def test_naming_robot(self):
        sys.stdout = StringIO()
        self.assertEqual(robot.get_robot_name(), "HAL")
        self.assertEqual(sys.stdout.getvalue().strip(), """What do you want to name your robot?""")


    def test_processing_inputs(self):
        self.assertTrue(robot.valid_commands("help"))
        self.assertTrue(robot.valid_commands("forward"))
        self.assertTrue(robot.valid_commands("off"))
        self.assertTrue(robot.valid_commands("HeLP"))
        self.assertTrue(robot.valid_commands("Forward 10"))
        self.assertFalse(robot.valid_commands("Jump"))
        self.assertFalse(robot.valid_commands("Hal"))
        self.assertFalse(robot.valid_commands("Fall over"))


    def test_help_call(self):
        #sys.stdout = StringIO()
        self.assertTrue(robot.show_help())
        self.assertEqual((True, """I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nFORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\nBACK - move backward by specified number of steps, e.g. 'BACK 10'\nRIGHT - turn right by 90 degrees\nLEFT - turn left by 90 degrees\nSPRINT - sprint forward according to a formula\nREPLAY - Redo all the steps in the history\nREPLAY SILENT - Redo all the steps in the history but supress the movements only returning the output\nMAZERUN - The robot will complete the maze, and make it to the outside"""), robot.show_help())

    
    def test_adding_history(self):
        robot.history = []
        self.assertEqual(robot.add_history("back 10"), ['back 10'])
        self.assertEqual(robot.add_history("forward 10"), ['back 10', 'forward 10'])


    def test_replay(self):
        robot.history = []
        robot.add_history("forward 10")
        robot.add_history("forward 5")
        robot.add_history("forward 5")        
        robot.add_history("forward 10")
        robot.add_history("forward 5")
        robot.add_history("sprint 3")
        self.assertEqual((True, """ > Hal replayed 6 commands."""),robot.do_replay("Hal", "replay", False, False))

    
    def test_silent_replay(self):
        robot.history = []
        robot.add_history("forward 10")
        robot.add_history("forward 5")
        robot.add_history("forward 5")        
        robot.add_history("forward 10")
        self.assertEqual((True, """ > Hal replayed 4 commands silently."""),robot.do_replay("Hal", "replay silent", True, False))


    def test_replay_reverse(self):
        robot.history = []
        robot.add_history("forward 10")
        robot.add_history("forward 5")
        robot.add_history("forward 5")        
        robot.add_history("forward 10")
        robot.add_history("forward 5")
        robot.add_history("sprint 3")
        self.assertEqual((True, """ > Hal replayed 6 commands in reverse."""),robot.do_replay("Hal", "replay", False, True))


    def test_replay_reverse_silent(self):
        robot.history = []
        robot.add_history("forward 10")
        robot.add_history("forward 5")
        robot.add_history("forward 5")        
        robot.add_history("forward 10")
        self.assertEqual((True, """ > Hal replayed 4 commands in reverse silently."""),robot.do_replay("Hal", "replay reverse silent", True, True))

    
    def test_replay_limited_range(self):
        robot.history = []
        robot.add_history("forward 3")
        robot.add_history("forward 2")
        robot.add_history("forward 1")
        self.assertEqual((True, """ > Hal replayed 2 commands in reverse."""),robot.do_replay("Hal", "replay reversed 2", False, True))
        self.assertEqual((True, """ > Hal replayed 2 commands."""),robot.do_replay("Hal", "replay 2", False, False))
        self.assertEqual((True, """ > Hal replayed 2 commands silently."""),robot.do_replay("Hal", "replay silent 2", True, False))
        self.assertEqual((True, """ > Hal replayed 1 commands in reverse silently."""),robot.do_replay("Hal", "replay reversed silent 2-1", True, True))


    def test_split_arg(self):
        self.assertEqual((True, False), robot.split_on_dash("3--a"))
        self.assertEqual(("3", "1"), robot.split_on_dash("3-1"))

        
if __name__ == '__main__':
    unittest.main()