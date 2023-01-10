from point import Point
from vector import Vector

class Label:
    def __init__(self, pointA, relpointB):
        self.startPoint=pointA
        self.endPoint=self.startPoint.newFromPoint(relpointB)
        self.center=self.startPoint.newFromCoords(relpointB.x/2,relpointB.y/2)
        self.is_assigned=False
    
    def distanceToLabel(self,labelB):
        return self.center.distance(labelB.center)
    
    def vectorToLabel(self,labelB):
        return self.center.vectorTo(labelB.center)
    
    def vectorFromLabel(self,labelB):
        return self.center.vectorFrom(labelB.center)
