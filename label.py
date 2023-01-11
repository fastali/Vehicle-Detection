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
        return self.center.distance(pointA)
    
    def getSize(self):
        return (self.endPoint.x-self.startPoint.x)*(self.endPoint.y-self.startPoint.y)
    
    def getLongestPrependicularDistanceToEdge(self):
        xline=self.center.x-self.startpoint.x
        yline=self.center.y-self.startpoint.y
        if(xline>yline):
            return xline
        return yline
    
    def isInRange(self,multiplyer,pointA):
        distance=self.distanceToCenter(pointA)
        if(multiplyer*self.getLongestPrependicularDistanceToEdge()<distance):
            return False
        return True
        
