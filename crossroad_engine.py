from vehicle import Vehicle
from label import Label
from point import Point
from vector import Vector

class CrossroadEngine:
    
    def __init__(self,hardlines):
        self.hardlines=hardlines
        self.vehicles=[]
        self.generateDirectionCounts()
        
    
    def generateDirectionCounts(self):
        self.directionCounts=[]
        for i in self.hardlines:
            self.directionCounts.append([0,0])
            
    @staticmethod
    def hardline_list_to_vector(lhardlines):
        vhardlines=[]
        for i in lhardlines:
            vhardlines.append(Vector(Point(i[0],i[1]),Point(i[2],i[3])))
        
    @staticmethod
    def coords_to_label(coords):
         return Label(Point(coords[0],coords[1]),Point(coords[2],coords[3]))
    
    @staticmethod
    def coords_to_labels(coordslist):
        labels=[]
        for i in coordslist:
            labels.append(CrossroadEngine.coords_to_label(i))
        return labels
            
    def generateVehicle(self,label):
        newVehicle= Vehicle()
        newVehicle.addLabel(label)
        self.vehicles.append(newVehicle)
            
    def analiseFrames(self,coordslist):
        labels=CrossroadEngine.coords_to_labels(coordslist)
        if(self.vehicles==[]):
            for i in labels:
                self.generateVehicle(i)
            return
        
        for i in self.vehicles:
            if(i.remove_counter==6):
                self.vehicles.remove(i)
                continue
            i.findlabels(labels)
            for j in range(len(self.hardlines)):
                result=i.hardlineCrossed(labels,self.hardlines[j])
                if(result==None):
                    continue
                if(result):
                    self.directionCounts[j][0]+=1
                    break
                self.directionCounts[j][1]+=1
                break
    
    def printCounts(self):
        for i in range(len(self.directionCounts)):
            print(f"{i+1} yönünde giden araç sayısı: {self.directionCounts[i][0]}")
            print(f"{i+1} yönünden gelen araç sayısı: {self.directionCounts[i][1]}")
            
                

                
