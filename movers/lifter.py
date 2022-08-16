from pybricks.ev3devices import Motor


class Lifter:
    def __init__(self, port):
        self.motor = Motor(port)
        self.speed = 360
        self.deg_per_step = 573
        self.pos = -1
        self.motor.run_until_stalled(-self.speed, duty_limit=20)
        self.motor.run_angle(self.speed, 50)

    def test(self):
        self.motor.run_angle(self.speed, -430*4)

    def set_mode(self, mode):
        self.motor.run_until_stalled(-self.speed, duty_limit=20)
        self.motor.run_angle(self.speed, 50)
        if mode == "READING":
            self.motor.run_angle(self.speed, 360*2)
            self.pos = 3

        if mode == "LIFTING":
            self.motor.run_angle(self.speed, 360*3+90)
            self.pos = 3

        if mode == "TURNING":
            self.pos = -1

    def set_pos(self, pos):
        assert pos >= 0 and pos <= 3
        assert self.pos >= 0 and self.pos <= 3
        steps = self.pos - pos
        self.motor.run_angle(self.speed, self.deg_per_step * steps)
        self.pos = pos
