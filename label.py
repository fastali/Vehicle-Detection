class Label:
    def __init__(self, pointA, relpointB):
        self.startPoint=pointA
        self.endPoint=self.startPoint.newFromPoint(relpointB)
        self.center=self.startPoint.newFromCoords(relpointB.x/2,relpointB.y/2)
        self.isAssigned=False
    
    def distanceToLabel(self,labelB):
        return self.center.distance(labelB.center)
    
    def vectorToLabel(self,labelB):
        return self.center.vectorTo(labelB.center)
    
    def vectorFromLabel(self,labelB):
        return self.center.vectorFrom(labelB.center)
    
    def isWithinFrame(self,pointA):
        if((self.startPoint.x<pointA.x) and  (self.endPoint.x>pointA.x) and (self.startPoint.y<pointA.y) and (self.endPoint.y>pointA.y)):
            return True
        return False
    
    def distanceToCenter(self,pointA):
        return self.center.distance(PointA)
