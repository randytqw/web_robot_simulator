from flask import Flask
from flask import request
from web_robot_parser import parse
from robot import Robot

app = Flask(__name__)

commands = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'RESET']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']


global_robot = Robot('', False, 0, 0)


@app.route("/")
def index():
    command = request.args.get('command', '')
    global global_robot
    if not command == '':
        global_robot = parse(command, global_robot)
    return ("""<form action="" method="get">
                <input type="text" name="command">
                <input type="submit" value="submit">
              </form>""" + global_robot.report())


if __name__ == "__main__":
    app.debug = True
    app.run()
# main()
