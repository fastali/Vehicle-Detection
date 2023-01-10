from vehicle import Vehicle

class CrossroadEngine:
    
    def __init__(self,hardlines):
        self.hardlines=hardlines
        self.vehicles=[]
        self.generateDirectionCounts()
        
    
    def generateDirectionCounts(self):
        self.directionCounts=[]
        for i in self.hardlines:
            self.directionCounts.append([0,0])
            
    def generateVehicle(self,label):
        newVehicle= Vehicle()
        newVehicle.addLabel(label)
            
    def analiseFrames(self,labels):
        if(self.vehicles==[]):
            for i in labels:
                self.vehicles.append(generateVehicle(i))
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
            
                

                
