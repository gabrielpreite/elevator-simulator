from Elevator import Elevator
import time

a = Elevator(0, 0)
a.setDest(5)
while(True):
    if(a.getOpen() == 0): #closed doors
        if(a.getDest() > a.getFloor()):
            a.setFloor(a.getFloor() + 1)
        elif(a.getDest() < a.getFloor()):
            a.setFloor(a.getFloor() - 1)
        elif(a.getDest() == a.getFloor()):
            a.setOpen(1)
    else: #open doors
        if(a.getDest() != a.getFloor()):
            a.setOpen(0)
    print("Floor: " + str(a.getFloor()) + ", Open: " + str(a.getOpen()))
    time.sleep(1)