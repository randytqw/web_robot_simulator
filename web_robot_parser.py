commands = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'RESET']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']


def parse(line, robot):
    input = line.split()
    if input[0] not in commands:
        print('invalid command')
        return robot
    if input[0] == 'PLACE':
        try:
            params = input[1].split(',')
            # check variable types
            if not params[0].isdigit() or not params[1].isdigit() or not params[2] in directions:
                print('invalid command')
                return robot
            return placeCommand(params, robot)
        except:
            raise Exception
    elif input[0] == 'LEFT' and len(input) == 1:
        return leftCommand(robot)
    elif input[0] == 'RIGHT' and len(input) == 1:
        return rightCommand(robot)
    elif input[0] == 'MOVE' and len(input) == 1:
        return moveCommand(robot)
    elif input[0] == 'RESET' and len(input) == 1:
        return resetCommand(robot)
    return robot
    # elif input[0] == 'REPORT' and len(input) == 1:
    # return reportCommand(robot)


def placeCommand(params, robot):
    if int(params[0]) > 4 or int(params[0]) < 0 or int(params[1]) > 4 or int(params[1]) < 0:
        raise Exception
    return robot.place(params)


def leftCommand(robot):
    return robot.rotateLeft()


def rightCommand(robot):
    return robot.rotateRight()


def moveCommand(robot):
    return robot.move()


def resetCommand(robot):
    return robot.reset()
