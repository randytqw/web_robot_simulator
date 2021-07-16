class Robot:
    def __init__(self, direction, placed, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.placed = placed

    def rotateLeft(self):
        if self.placed == False:
            return self
        elif self.direction == 'NORTH':
            self.direction = 'WEST'
        elif self.direction == 'WEST':
            self.direction = 'SOUTH'
        elif self.direction == 'SOUTH':
            self.direction = 'EAST'
        elif self.direction == 'EAST':
            self.direction = 'NORTH'
        return self

    def rotateRight(self):
        if self.placed == False:
            return self
        elif self.direction == 'NORTH':
            self.direction = 'EAST'
        elif self.direction == 'WEST':
            self.direction = 'NORTH'
        elif self.direction == 'SOUTH':
            self.direction = 'WEST'
        elif self.direction == 'EAST':
            self.direction = 'SOUTH'
        return self

    def move(self):
        if self.placed == False:
            return self
        elif self.direction == 'NORTH' and self.y < 4:
            self.y = self.y + 1
            return self
        elif self.direction == 'SOUTH' and self.y > 0:
            self.y = self.y - 1
            return self
        elif self.direction == 'WEST' and self.x > 0:
            self.x = self.x - 1
            return self
        elif self.direction == 'EAST' and self.x < 4:
            self.x = self.x + 1
            return self
        return self

    def report(self):
        if self.placed == False:
            return "not placed"
        report = 'x=%d y=%d f=%s' % (self.x, self.y, self.direction)
        return report

    def place(self, params):
        self.placed = True
        self.x = int(params[0])
        self.y = int(params[1])
        self.direction = params[2]
        return self

    def reset(self):
        self.placed = False
        self.x = 0
        self.y = 0
        self.direction = ''
        return self
