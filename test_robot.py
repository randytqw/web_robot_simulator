import unittest
from robot import Robot
from web_robot_parser import parse


class test_robot(unittest.TestCase):
    # def setUp(self):
    '''
    Passing Test Cases
    '''

    def testRobotInit(self):
        robot = Robot('', False, 0, 0)
        self.assertEqual(robot.direction, '')
        self.assertEqual(robot.placed, False)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)

    def testRobotRotateLeft(self):
        robot = Robot('NORTH', True, 0, 0)
        robot = robot.rotateLeft()
        self.assertEqual(robot.direction, 'WEST')

    def testRobotRotateRight(self):
        robot = Robot('NORTH', True, 0, 0)
        robot = robot.rotateRight()
        self.assertEqual(robot.direction, 'EAST')

    def testRobotMoveX(self):
        robot = Robot('EAST', True, 0, 0)
        robot = robot.move()
        self.assertEqual(robot.x, 1)

    def testRobotMoveY(self):
        robot = Robot('NORTH', True, 0, 0)
        robot = robot.move()
        self.assertEqual(robot.y, 1)

    def testRobotPlace(self):
        robot = Robot('', False, 0, 0)
        robot = robot.place([1, 1, 'NORTH'])
        self.assertEqual(robot.direction, 'NORTH')
        self.assertEqual(robot.placed, True)
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)

    def testParsePlace(self):
        robot = Robot('', False, 0, 0)
        robot = parse('PLACE 0,0,NORTH', robot)
        self.assertEqual(robot.direction, 'NORTH')
        self.assertEqual(robot.placed, True)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)

    '''
    Failing Test Cases
    '''

    def testNotPlaced(self):
        robot = Robot('', False, 0, 0)
        robot = robot.rotateRight()
        self.assertEqual(robot.direction, '')
        self.assertEqual(robot.placed, False)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)

    def testInvalidMove(self):
        robot = Robot('WEST', True, 0, 0)
        robot = robot.move()
        self.assertEqual(robot.direction, 'WEST')
        self.assertEqual(robot.placed, True)
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)


unittest.main()
