
<<<<<<< Updated upstream
=======
<<<<<<< Updated upstream
import defs.Robot_Control.control2Robots;
import defs.Robot_Control.conveyorR2;
import defs.Robot_Control.conveyorSensors;
import defs.Robot_Control.detect2Objects;
import defs.Robot_Control.Gripper;
import defs.Robot_Control.pickAndPlaceR1;
import defs.states;
=======
>>>>>>> Stashed changes
# import defs.Robot_Control.control2Robots
# import defs.Robot_Control.conveyorR2
# import defs.Robot_Control.conveyorSensors
# import defs.Robot_Control.detect2Objects
# import defs.Robot_Control.Gripper
# import defs.Robot_Control.pickAndPlaceR1
# import defs.states
import numpy as np



id = 0 
posX = 0 
posY = 0
blockWidth = 0 
gridOfBlocks = np.array([[id, posX, posY]])

def initialBlockPositions():
    id = 0
    posX = 0
    posY = 0
    blockWidth = 0.05

def determineBlockType(BlockType):
    if BlockType == 'cube': workSpace = 1
    elif BlockType =='cylinder': workSpace = 2
<<<<<<< Updated upstream
=======
    return
>>>>>>> Stashed changes

def determineNextPosition(i, blockWidth, posX, posY):
        if i < 4:
            posX += blockWidth
        elif i > 4 and i < 11:
            posY += blockWidth
        elif i > 10 and i < 15:
            posX -= blockWidth
        elif i > 15 and i < 21:
            posY -= blockWidth
<<<<<<< Updated upstream

def storeBlockLocatation(i, posX, posY):
    np.append(gridOfBlocks, [[i, posX, posY]], axis=1)
=======
        return

def storeBlockLocatation(i, posX, posY):
    np.append(gridOfBlocks, [[i, posX, posY]], axis=1)
    return
>>>>>>> Stashed changes

def createGridOfBlocks(BlockType, totalNumberOfBlocksStored):
    determineBlockType(BlockType)
    initialBlockPositions()
<<<<<<< Updated upstream
=======
    
>>>>>>> Stashed changes
       
    for i in range(totalNumberOfBlocksStored):
        storeBlockLocatation(i, posX, posY)
        determineNextPosition(i, blockWidth, posX, posY)
    return gridOfBlocks


print(createGridOfBlocks('cube', 10))





<<<<<<< Updated upstream
=======
>>>>>>> Stashed changes
>>>>>>> Stashed changes

