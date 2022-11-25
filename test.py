import defs.Robot_Control.conveyorSensors as cS
import defs.Robot_Control.conveyorR2 as conveyor
import time

def startConveyorWhenBlockPlaced():
    sensorLeft = cS.checkConveyorSensor(cS.sensorLeft)
    sensorRight = cS.checkConveyorSensor(cS.sensorRight)
    sensorMiddleLeft = cS.checkConveyorSensor(cS.sensorMiddleLeft)
    sensorMiddleRight = cS.checkConveyorSensor(cS.sensorMiddleRight)
    if sensorLeft < 50:
        # No object in front of sensor left side 
        if sensorRight > 50:
            # No object in front of sensor right side - Ok to travel left to right
            if sensorMiddleRight > 50:
                # No object in front of sensor middle right
                if sensorMiddleLeft > 50:
                    # Initial start position
                    conveyor.setConveyorSpeed(0.05)
                    conveyor.startConveyor()
                    conveyor.time.sleep(1)
                    conveyor.stopConveyor()
                    conveyor.rob2.close()

while True:
    startConveyorWhenBlockPlaced()
    time.sleep(1)
