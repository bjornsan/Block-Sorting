def isPreSorting():
    return

def isPostSorting():
    return

def isTransporting():
    return

def isMoving():
    return


def determineAvailibleRobots():
    if isTransporting() == True: 
        print("Conveyor belt busy - During transport")
        if isPreSorting() == True: 
            print("Pre sorting - During transport")
        if isPostSorting() == True: 
            print("Post sorting - During transport")
        if isMoving() == True: 
            print("Moving - During transport")
        else:
            print("Not sorting - During transport")

    else:
        print("Conveyor belt idle - Ready for transport")
        if isPreSorting() == True: 
            print("Pre sorting - idle conveyor belt")
        if isPostSorting() == True: 
            print("Post sorting - idle conveyor belt")
        if isMoving() == True: 
            print("Moving - idle conveyor belt")
        else:
            print("Not sorting - idle conveyor belt")   
