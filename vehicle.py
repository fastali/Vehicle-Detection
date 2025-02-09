from vector import Vector

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
        return self.labels[-1]
    
    def findLabels(self,frame_labels):
        self.remove_counter+=1
        if(len(self.labels)==0):
            return
        last_label=self.getLastLabel()
        best_candidate=None
        for i in frame_labels:
            if(i.isAssigned):
                continue
            if((i.isInRange(2,last_label.center))==False):
                continue
            if(best_candidate==None):
                best_candidate=i
                continue
            if(last_label.distanceToLabel(best_candidate)>last_label.distanceToLabel(i)):
                best_candidate=i
        if(best_candidate==None):
            return
        self.addLabel(best_candidate)
           
    def hardlineCrossed(self,frame_labels,hardline):
        if(len(self.labels)<2):
            return None
        last_movement=Vector(self.labels[-2].center,self.labels[-1].center)
        if(last_movement.isLineCrossed(hardline)):
            return last_movement.isCrossDirectionInward(hardline)
        return None
            
        
        
        
        
        
        
