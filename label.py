from point import Point

class Label:
  def __init__(self, pointA, relpointB):
    self.startPoint=pointA
    self.endPoint=self.startPoint.fromPoint(relpointB)
  
    
