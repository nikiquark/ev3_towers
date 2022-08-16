#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port


from movers.turner import Turner
from movers.claw import Claw
from movers.lifter import Lifter
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()

lifter = Lifter(Port.C)
claw = Claw(Port.A)
turner = Turner(Port.D, 250)


def move(a, b):
    assert lifter.pos == -1
    turner.set_pos(a[0])
    lifter.set_mode("LIFTING")
    lifter.set_pos(a[1])
    claw.close()
    lifter.set_mode("TURNING")
    turner.set_pos(b[0])
    lifter.set_mode("LIFTING")
    lifter.set_pos(b[1])
    claw.open()
    lifter.set_mode("TURNING")


turns = [
    ((0, 3), (1, 0)), ((0, 2), (2, 0)),
    ((1, 0), (2, 1)), ((0, 1), (1, 0)),
    ((2, 1), (0, 1)), ((2, 0), (1, 1)),
    ((0, 1), (1, 2)), ((0, 0), (2, 0)),
]

for (a, b) in turns:
    move(a, b)
