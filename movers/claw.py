from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

class Claw:
    def __init__(self, port):
        self.motor = Motor(port)
        self.speed = 60
        # self.deg90 = 440
        self.motor.run_until_stalled(-self.speed, duty_limit = 10)
        self.motor.run_angle(self.speed, 90)
        self.is_open = True
        

    def close(self):
        if self.is_open:
            self.motor.run_angle(self.speed, -90)
            self.is_open = False

    def open(self):
        if not self.is_open:
            self.motor.run_angle(self.speed, 90)
            self.is_open = True
