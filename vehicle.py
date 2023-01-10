from label import Label
from vector import Vector
from point import Point

class Vehicle:
    def __init__(self):
        self.labels=[]
        self.remove_counter=0
  
    def addLabel(self,vlabel):
        self.labels.append(vlabel)
        vlabel.isAssigned=True
        self.remove_counter=0
  
    def getLastLabel(self):
        if(len(self.labels)==0):
            return None
        return labels[-1]
    
    def findLabels(self,frame_labels):
        self.remove_counter+=1
        if(len(self.labels)==0):
            return
        last_label=self.getLastLabel()
        best_candidate=None
        for i in frame_labels:
            if(i.isAssigned):
                continue
            if(!i.isWithinFrame()):
                continue
            if(best_candidate==None):
                best_candidate=i
                continue
            if(last_label.distanceToLabel(best_candidate)>last_label.distanceToLabel(i)):
                best_candidate=i
        if(best_candidate==None):
            return
        self.addLabel(best_candidate)
           
    def hardlineCrossed(self,frame_labels,hardlines):
        findLabels(frame_labels)
        if(len(self.labels)<2):
            return None
        last_movement=Vector(self.labels[-2],self.labels[-1])
        for i in hardlines:
            if(last_movement.isLineCrossed(i)):
                return last_movement.isCrossDirectionInward(i)
        return None
            
        
        
        
        
        
        
