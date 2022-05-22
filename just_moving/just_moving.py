#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
# vex-vision-config:begin
vision_5 = Vision(Ports.PORT5, 50)
# vex-vision-config:end
potentiometer_a = Potentiometer(brain.three_wire_port.a)
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
frontLeftMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
frontRightMotor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)






#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *



# Begin project code
class Settings:
    def __init__(self):
        self.setup()

    def controller_R2_Pressed(self):
        arm_motor.spin(REVERSE)
        while controller_1.buttonR2.pressing():
            wait(5, MSEC)
        arm_motor.stop()

    def controller_R1_Pressed(self):
        arm_motor.spin(FORWARD)
        while controller_1.buttonR1.pressing():
            wait(5, MSEC)
        arm_motor.stop()
        
    def controller_L2_Pressed(self):
        claw_motor.spin(FORWARD)
        while controller_1.buttonL2.pressing():
            wait(5, MSEC)
        claw_motor.stop()

    def controller_L1_Pressed(self):
        claw_motor.spin(REVERSE)
        while controller_1.buttonL1.pressing():
            wait(5, MSEC)
        claw_motor.stop()



    def setup(self):
        controller_1.buttonR2.pressed(self.controller_R2_Pressed)
        controller_1.buttonR1.pressed(self.controller_R1_Pressed)
        controller_1.buttonL2.pressed(self.controller_L2_Pressed)
        controller_1.buttonL1.pressed(self.controller_L1_Pressed)

        wait(15, MSEC)
        arm_motor.set_stopping(HOLD)

def openClaw():
    claw_motor.spin(REVERSE)
    while not claw_motor.is_spinning():
        pass
    claw_motor.stop()
    pass

def closeClaw():
    claw_motor.spin(FORWARD)
    while not claw_motor.is_spinning():
        pass
    claw_motor.stop()
    pass


def moveCheck():
    x = controller_1.axis3.position()
    y = controller_1.axis4.position()
    frontLeftMotor.set_velocity(y + x, PERCENT)
    frontLeftMotor.spin(FORWARD)

    frontRightMotor.set_velocity(y - x, PERCENT)
    frontRightMotor.spin(FORWARD)
    
    wait(20, MSEC)

# def loggingPotentiometer():
#     brain.screen.print("Angle - Degrees:", potentiometer_a.angle(DEGREES))
#     brain.screen.next_row()

#     brain.screen.print("Angle - Percent:", potentiometer_a.angle(PERCENT))
#     brain.screen.next_row()


def main():
    settings = Settings()
    while True:
        moveCheck()

main()