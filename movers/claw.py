from pybricks.ev3devices import Motor


class Claw:
    def __init__(self, port):
        self.motor = Motor(port)
        self.speed = 60
        self.deg_per_step = 70
        self.motor.run_until_stalled(-self.speed, duty_limit=10)
        self.motor.run_angle(self.speed, self.deg_per_step)
        self.is_open = True

    def close(self):
        if self.is_open:
            self.motor.run_angle(self.speed, -self.deg_per_step)
            self.is_open = False

    def open(self):
        if not self.is_open:
            self.motor.run_angle(self.speed, self.deg_per_step)
            self.is_open = True
