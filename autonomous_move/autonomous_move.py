#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code


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
        arm_motor.spin(FORWARD)
        while controller_1.buttonR2.pressing():
            wait(5, MSEC)
        arm_motor.stop()

    def controller_R1_Pressed(self):
        arm_motor.spin(REVERSE)
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

    def controller_B_Pressed(self):
        self.image_checking = not self.image_checking;


    def setup(self):
        controller_1.buttonR2.pressed(self.controller_R2_Pressed)
        controller_1.buttonR1.pressed(self.controller_R1_Pressed)
        controller_1.buttonL2.pressed(self.controller_L2_Pressed)
        controller_1.buttonL1.pressed(self.controller_L1_Pressed)
        controller_1.buttonB.pressed(self.controller_B_Pressed)
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
class Autonomous:
    def __init__(self):
        self.rotateZ = FORWARD
        self.rotateArm = FORWARD
        self.rotateClaw = FORWARD

    def move(self):
        # print('move')
        # closeClaw()
        #rotire masina
        frontLeftMotor.set_velocity(10, PERCENT)
        frontRightMotor.set_velocity(10, PERCENT)

        frontLeftMotor.spin(
            (FORWARD if self.rotateZ == FORWARD else REVERSE)
        );
        frontRightMotor.spin(
            ( FORWARD if self.rotateZ == FORWARD else FORWARD)
            
        );

        self.rotateZ = (
            REVERSE if self.rotateZ == FORWARD else FORWARD
            )

        #rotire brat
        # print(self.rotateArm)
        arm_motor.spin(self.rotateArm)
        self.rotateArm = (
            REVERSE if self.rotateArm == FORWARD else FORWARD
            )

        #inchide si deschide gheara
        claw_motor.spin(self.rotateClaw)
        self.rotateClaw = (
            REVERSE if self.rotateClaw == FORWARD else FORWARD
        )
        wait(1,SECONDS)


def moveCheck():
    x = controller_1.axis3.position()
    y = controller_1.axis4.position()
    frontLeftMotor.set_velocity(y + x, PERCENT)
    frontLeftMotor.spin(FORWARD)

    frontRightMotor.set_velocity(y - x, PERCENT)
    frontRightMotor.spin(FORWARD)
    
    wait(20, MSEC)


def imageCheck():    
    frontLeftMotor.set_velocity(15, PERCENT)
    frontRightMotor.set_velocity(15, PERCENT)
    camera_offset= 0;
    print('before vision detection')
    vision_object = vision_5.take_snapshot(vision_5__RED_COLA)
    if vision_object is not None:
        vision_object_detected = vision_5.largest_object()
        print('object found')
        print(vision_object_detected.centerX)
        if vision_object_detected.centerX >100 + camera_offset:
            #turn right
            frontLeftMotor.spin(FORWARD);
            frontRightMotor.spin(REVERSE);
            pass
        elif vision_object_detected.centerX <60 + camera_offset:
            #turn left
            frontLeftMotor.spin(FORWARD);
            frontRightMotor.spin(REVERSE);
        else :
            if vision_object_detected.width < 7:
                #drive toward
                frontLeftMotor.spin(FORWARD);
                frontRightMotor.spin(FORWARD);
            else:
                #stop
                frontLeftMotor.stop();
                frontRightMotor.stop();
    else:
        print('not found object')
    wait(500, MSEC)

# def loggingPotentiometer():
#     brain.screen.print("Angle - Degrees:", potentiometer_a.angle(DEGREES))
#     brain.screen.next_row()

#     brain.screen.print("Angle - Percent:", potentiometer_a.angle(PERCENT))
#     brain.screen.next_row()


def main():
    settings = Settings()
    autonomous = Autonomous()
    openClaw()
    while True:
        if(settings.autonomous_drive == True):
            autonomous.move()

main()