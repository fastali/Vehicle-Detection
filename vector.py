class Vector:
  
    def __init__(self,pointA,pointB):
        self.startpoint=pointA
        self.endpoint=pointB
  
    def lenght(self):
        return self.startpoint.distance(self.endpoint)
    
    @staticmethod
    def is_counter_clockwise(PointA,PointB,PointC):
        return (PointC.y-PointA.y) * (PointB.x-PointA.x) > (PointB.y-PointA.y) * (PointC.x-PointA.x)
    
    def isLineCrossed(self,VectorB):
        Condition1 = Vector.is_counter_clockwise(self.startpoint,VectorB.startpoint,VectorB.endpoint) != Vector.is_counter_clockwise(self.endpoint,VectorB.startpoint,VectorB.endpoint)
        Condition2 = Vector.is_counter_clockwise(self.startpoint,self.endpoint,VectorB.startpoint) != Vector.is_counter_clockwise(self.startpoint,self.endpoint,VectorB.endpoint)
        return Condition1 and Condition2
    
    def isCrossDirectionInward(self,VectorB):
        return Vector.is_counter_clockwise(self.startpoint,self.endpoint,VectorB.startpoint)
        
      
