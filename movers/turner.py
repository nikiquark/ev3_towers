from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait


class Turner:

    def __init__(self, port, speed, pos = None):
        self.motor = Motor(port)
        self.speed = speed
        self.deg90 = 440
        if pos is None:
            self.motor.run_until_stalled(self.speed, duty_limit = 30)
            self.pos = 0
        else:
            self.pos = pos 

    def set_pos(self, pos):
        steps = self.pos - pos
        if steps != 0 and pos == 0:
             self.motor.run_until_stalled(self.speed, duty_limit = 30)
        else:
            self.motor.run_angle(self.speed, steps*self.deg90)
        self.pos = pos
        
    def test(self):
        pass
