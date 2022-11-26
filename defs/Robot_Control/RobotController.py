import urx
from Gripper import *
#import urllib.request
import time
import ConveyorController as CC

sentBlocks = 0
pos_multiplyer = 0.06
block_y_pos = -0.22 - (sentBlocks*pos_multiplyer)


def pickUpFromConveyor(rob):
    global block_y_pos

    #positions x, y, z, rx, ry, rz
    pos1 = 0.10, -0.30, 0.40, 0, 3.14, 0
    pos2 = 0.20, 0.10, 0.40, 0, 3.14, 0
    pos3 = 0.03, 0.30, 0.40, 0, 3.14, 0
    pos4 = 0.03, 0.30, 0.25, 0, 3.14, 0
    pos5 = 0.03, 0.30, 0.15, 0, 3.14, 0
    
    pos6 = 0.25, block_y_pos, 0.30, 0, 3.14, 0
    pos7 = 0.25, block_y_pos, 0.20, 0, 3.14, 0
    


    move(rob, pos1, True)
    move(rob, pos2, True)
    move(rob, pos3, True)
    move(rob, pos4, True)
    move(rob, pos5, True)

    rob.send_program(rq_close())
    time.sleep(3)

    move(rob, pos4, True)
    move(rob, pos3, True)
    move(rob, pos2, True)
    move(rob, pos1, True)
    move(rob, pos6, True)
    move(rob, pos7, True)

    rob.send_program(rq_open())
    time.sleep(2)

    move(rob, pos6, True)
    move(rob, pos1, True)

    
def sendLeftToRight(rob):
    sensorvalue = 0
    sensorValue = CC.checkSensorReadingsLeft()
    time.sleep(2)
    print("DONE CHECKING SENSORS")
    if sensorValue != 0 or sensorValue != None:
        print("INSIDE IF")
        pickUpFromConveyor(rob)
        global sentBlocks, block_y_pos 
        sentBlocks += 1
        block_y_pos = -0.22 - (sentBlocks*pos_multiplyer)

    print("DONE WITH sendLeftToRight")

def sendRightToLeft():
    CC.checkSensorReadingsRight()
    


def move(robot, location, moveWait):
    #moves robot
    robot.movex("movel", location,wait=moveWait, acc=0.5, vel=0.8, relative=False, threshold=None)
    if moveWait == False:
        time.sleep(0.1)



if __name__ =="__main__":
    r1="10.1.1.5"
    #connects to robot
    rob = urx.Robot(r1, use_rt=True, urFirm=5.1)

    #activates gripper. only needed once per power cycle
    rob.send_program(rq_activate())
    time.sleep(2.5)
    #sets speed of gripper to max
    rob.send_program(rq_set_speed(1))
    time.sleep(0.1)
    #sets force of gripper to a low value
    rob.send_program(rq_set_force(10))
    time.sleep(0.1)
    rob.send_program(rq_open())
    time.sleep(2)

    for i in range(4):
        sendLeftToRight(rob)
        time.sleep(2)

    rob.close()