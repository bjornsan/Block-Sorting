import defs.Robot_Control.conveyorSensors as cS
import defs.Robot_Control.conveyorR2 as conveyor
import time

def startConveyorWhenBlockPlaced():
    sensorLeft = cS.checkConveyorSensor(cS.sensorLeft)
    sensorRight = cS.checkConveyorSensor(cS.sensorRight)
    sensorMiddleLeft = cS.checkConveyorSensor(cS.sensorMiddleLeft)
    sensorMiddleRight = cS.checkConveyorSensor(cS.sensorMiddleRight)

    if int(sensorLeft) < 50:
        print(sensorLeft)
        # Initial start position
        #conveyor.setConveyorSpeed(0.05)
        #conveyor.startConveyor()
        #conveyor.time.sleep(1)
        #conveyor.stopConveyor()
        #conveyor.rob2.close()
         

while True:
    startConveyorWhenBlockPlaced()
    time.sleep(1)
