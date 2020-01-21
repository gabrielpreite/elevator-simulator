class Elevator:
    def __init__(self, number, floor):
        self.number = number
        self.floor = floor
        self.open = 1
        self.dest = floor

    def setFloor(self, n):
        self.floor = n
    
    def getFloor(self):
        return self.floor

    def setOpen(self, n):
        self.open = n
    
    def getOpen(self):
        return self.open

    def setDest(self, n):
        self.dest = n
    
    def getDest(self):
        return self.dest