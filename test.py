from vexcode import *
from vexcode import triport


DumperA = triport.DigitalPort('H')
def main():
    drivetrain.drive_for(FORWARD, 100, MM)
    if DumperA.pressed():
        drivetrain.drive_for(Forward)
        wait(5, SECONDS)
        drivetrain.stop()
vr_thread(main())