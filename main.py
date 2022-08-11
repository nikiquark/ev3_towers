#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from movers.turner import Turner
from movers.claw import Claw
from movers.lifter import Lifter
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# turner = Turner(Port.D, 250)
lifter = Lifter(Port.C)
claw = Claw(Port.A)

lifter.set_mode("LIFTING")
lifter.set_pos(0)
claw.close()
claw.open()
# Write your program here.

