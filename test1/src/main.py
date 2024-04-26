# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       wstenzel                                                     #
# 	Created:      4/25/2024, 1:04:43 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

from vex import *

# Brain should be defined by default
brain = Brain()

# 
#

# The controller
controller = Controller()

# Drive motors
left_drive_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)


# Max motor speed (percent) for motors controlled by buttons
MAX_SPEED = 100

#
# All motors are controlled from this function which is run as a separate thread
#


def vex.Bumper.__init__	(	 	self,
 	triport_port 
)		

bumperA = vex.Bumper(Brain.ThreeWirePort.A)

def drive_task():
    if Bumper.changed()==True:
       
        
# Run the drive code
drive = Thread(drive_task)

# Python now drops into REPL
