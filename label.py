from point import Point

class Label:
    def __init__(self, pointA, relpointB):
        self.startPoint=pointA
        self.endPoint=self.startPoint.newFromPoint(relpointB)
        self.center=self.startPoint.newFromCoords(relpointB.x/2,relpointB.y/2)
    
  
    
