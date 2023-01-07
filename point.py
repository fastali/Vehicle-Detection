
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def distance(self,pointB):
        return (((self.x-pointB.x)**2)+((self.y-pointB.y)**2))**0.5
  
    def newFromPoint(self,relpointB):
        return Point(self.x+relpointB.x,self.y+relpointB.y)
    
    def newFromCoords(self,x,y):
        return Point(self.x+x,self.y+y)
