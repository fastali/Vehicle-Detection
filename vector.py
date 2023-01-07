class Vector:
  
    def __init__(self,pointA,pointB):
        self.startpoint=pointA
        self.endpoint=pointB
  
    def lenght(self):
        return self.startpoint.distance(self.endpoint)
