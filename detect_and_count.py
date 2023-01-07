import os
import time

import numpy as np

from copy import deepcopy




def is_counter_clockwise(pointA,PointB,PointC):
  return (PointC[1]-PointA[1]) * (PointB[0]-PointA[0]) > (PointB[1]-PointA[1]) * (PointC[0]-PointA[0])

def is_line_crossed(hardline,movement_vector):
  PointA,PointB = vector_to_points(movement_vector)
  PointC,PointD = vector_to_points(hardline)
  Condition2 = is_counter_clockwise(PointA,PointC,PointD) != is_counter_clockwise(PointB,PointC,PointD)
  Condition2 = is_counter_clockwise(PointA,PointB,PointC) != is_counter_clockwise(PointA,PointB,PointD)
  return Condition1 and Condition2

def is_cross_direction_inward(hardline,movement_vector):
  PointA,PointB = vector_to_points(movement_vector)
  PointC,PointD = vector_to_points(hardline)
  return is_counter_clockwise(PointA,PointB,PointC)

def does_vector_cross_any_lines(hardlines,movement_vector,lines_crossed):
  for i in range(len(hardlines)):
    if(is_line_crossed(hardlines[i],movement_vector)):
      if(is_cross_direction_inward(hardlines[i],movement_vector)):
        lines_crossed[i,0]+=1
      else:
        lines_crossed[i,1]+=1
      return lines_crossed
  return lines_crossed

def do_vectors_cross_any_lines(hardlines,movement_vectors,lines_crossed):
  for i in movement_vectors:
    lines_crossed=does_vector_cross_any_lines(hardlines,i,lines_crossed)
  return lines_crossed

def filters(labels,hwtresh): #filter results
  for i in range(labels.shape[0]):
    if(labels[i,3]>hwtresh[1] or labels[i,3]<hwtresh[0] or labels[i,4]>hwtresh[3] or labels[i,4]<hwtresh[2]):
      labels=np.delete(labels,i,0)
  return labels

def calculate_label_center(label): #calculate the center point of the visible part of the vehicle 
  result= [label[1]+label[3]/2,label[2]+label[4]/2]
  return result

def calculate_movement_vector(pointA,pointB): #returns the vector that goes from point A to point B
  result=np.array([pointA[0],pointA[1],pointB[0],pointB[1]])
  return result

def calculate_distance(pointA,pointB): #returns the distance between point A and point B
  result=(((pointB[0]-pointA[0])**2)+((pointB[1]-pointA[1])**2))**0.5
  return result

def label_to_point(label):
  return [label[6],label[7]]

def vector_to_points(vec):
  PointA=[vec[0],vec[1]]
  PointB=[vec[2],vec[3]]
  return [PointA,PointB]
  
def calcuate_center(labels): #set the center locations of all the given vehicles
  for i in labels:
    i[6],i[7]=calculate_label_center(i)
  return labels
                                                       
                                                     
  

def match_labels(oldlabels,labels): #matches the vehicles with the vehicles from the previous frame
  matchtable=np.array([])
  if(oldlabels.size==0):
    return matchtable
  for i in range(labels.shape[0]):
    temp=np.finfo(labels.dtype).max
    match=-1
    for j in range(oldlabels.shape[0]):
      distance=calculate_distance(label_to_point(labels[i]),label_to_point(oldlabels[j]))
      if(temp>distance):
        is_actually_closest=True
        for k in range(labels.shape[0]):
          pos_distance=calculate_distance(label_to_point(labels[k]),label_to_point(oldlabels[j]))
          if(pos_distance<distance):
            is_actually_closest=False
            break
        if(is_actually_closest):
          temp=distance
          match=j
        else:
          continue
    if(match==-1):
      continue
    matchtable=np.r_[matchtable,np.array([i,match])]
  return matchtable
    
def generate_vectors(matchtable,oldlabels,labels): #produces the vectors from matched labels
  movement_vectors=np.zeros((matchtable.shape[0],4),dtype=float)
  for i in range(matchtable.shape[0]):
    movement_vectors[i]=calculate_movement_vector(label_to_point(labels[matchtable[i,0]]),label_to_point(oldlabels[matchtable[i,1]]))
  return movement_vectors

def print_lines_crossed(lines_crossed):
  print(f"güneyden gelen: {lines_crossed[0,0]}")
  print(f"doğudan gelen: {lines_crossed[1,0]}")
  print(f"doğudan kuzeye dönen: {lines_crossed[2,0]}")
  print(f"kuzeyden gelen: {lines_crossed[4,0]}")
  print(f"kuzeyden batıya dönen: {lines_crossed[5,0]}")
  print(f"güneye giden: {lines_crossed[0,1]}")
  print(f"kuzeye giden: {lines_crossed[3,1]}")
  print(f"batıya giden: {lines_crossed[6,1]}")
  
def estimate_flow(oldlabels,labels,hard_lines,lines_crossed,hwtreshold):
  if((labels.size==0) or (oldlabels.size==0)):
    return lines_crossed
  if(len(labels.shape)==1):
    labels=np.reshape(labels,(1,labels.shape[0]))
  if(len(oldlabels.shape)==1):
    oldlabels=np.reshape(oldlabels,(1,oldlabels.shape[0]))
  labels=filters(labels,hwtreshold)
  labels=np.c_[labels, np.zeros(labels.shape[0]) , np.zeros(labels.shape[0])]
  labels=calcuate_center(labels)
  matchtable=match_labels(oldlabels,labels)
  movement_vectors=generate_vectors(matchtable,oldlabels,labels)
  lines_crossed=do_vectors_cross_any_lines(hard_lines,movement_vectors,lines_crossed)
  return lines_crossed

def run(source_path,weights_path,hard_lines,hwtreshold,lines_crossed):
  labels=np.array([])
  labelsold=np.array([])
  tsec=time.time()
  freq=0
  while(True):
    os.system(f"python detect.py --weights {weights_path} --source {source_path} --save-txt --save-conf --nosave --line-thickness 1 --conf-thres 0.8")
    if(os.path.isfile("runs/detect/exp/labels/image.txt")):
      print("txt output file not found!")
      os.system(f"rm -rf runs/detect/exp/")
      if(time.time()-tsec>5.0):
        print(f"FPS: {freq/5.0}")
        freq=0
        print_lines_crossed(lines_crossed)
        tsec=time.time()
        continue
    with open("runs/detect/exp/labels/image.txt","r") as f:
      if(labels.size==0):
        labelsold=np.array([])
      else:
        labelsold=deepcopy(labels)
      labels=np.asarray([i.split() for i in f.readlines()], dtype=float)
    lines_crossed=estimate_flow(oldlabels,labels)
    freq+=1
    if(time.time()-tsec>5.0):
      print(f"FPS: {freq/5.0}")
      freq=0
      print_lines_crossed(lines_crossed)
      tsec=time.time()
    os.system(f"rm -rf runs/detect/exp/")


if __name__ == "__main__":
  #filter by size of the detected object (size is a ratio based on the image size, image size is assumed to be h=1.0,w=1.0 )
  hwtreshold=[0.01,0.5,0.01,0.5] 
  """
  hard lines are the locations in which if a vehicle crosses, a special counter is incremented. 
  Every hard line has 4 float values which can be mapped to the x y coordinates of the inputed frame.
  If we assume that every vector goes from Point A to Point B (coordinates are packed as such for each hard line [PointAx, PointAy, PointBx, PointBy]),
  every movement from right side of the vector towards the left side of the vector would be counted as an invard movement to the crossing and likely the oposite
  would be counted as an outward movement from the crossing. therefore hardline vector directions should be given accordingly
  """
  hard_lines=[[.235,.743,.9,.92],[.84,.72,.9,.92],[.755,.63,.74,.67],[0.61,.555,.53,.555],[0.5,0.676,0.37,0.65],[.325,.64,.33,.59],[.175,.59,.11,.68]]
  lines_crossed=np.zeros((len(hard_lines),2),dtype=int)
  weights="Vehicle-Detection/runs/train/exp12/weights/best.pt"
  source="image.jpg"
  run(source,weights,hard_lines,hwtreshold,lines_crossed) #runs until stopped
  
  
