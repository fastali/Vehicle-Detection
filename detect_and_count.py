import os

import numpy as np

from copy import deepcopy


hwtreshold=[0.01,0.5,0.01,0.5] #filter by size of the detected object (size is a ratio based on the image size, image size is assumed to be h=1.0,w=1.0 )
"""
  hard lines are the locations in which if a vehicle crosses, a special counter is incremented. 
  Every hard line has 4 float values which can be mapped to the x y coordinates of the inputed frame.
  If we assume that every vector goes from Point A to Point B (coordinates are packed as such for each hard line [PointAx, PointAy, PointBx, PointBy]),
  every movement from right side of the vector towards the left side of the vector would be counted as an invard movement to the crossing and likely the oposite
  would be counted as an outward movement from the crossing.
"""
hard_lines=[[.235,.743,.9,.92],[.84,.72,.9,.92],[.755,.63,.74,.67],[0.61,.555,.53,.555],[0.5,0.676,0.37,0.65],[.325,.64,.33,.59],[.175,.59,.11,.68]]

def filters(labels,hwtresh): #filter results
  for i in range(labels.shape[0]):
    if(labels[i,3]>hwtresh[1] or labels[i,3]<hwtresh[0] or labels[i,4]>hwtresh[3] or labels[i,4]<hwtresh[2]):
      labels=np.delete(labels,i,0)
  return labels

def calculate_label_center(label): #calculate the center point of the visible part of the vehicle 
  result= [label[1]+label[3]/2,label[2]+label[4]/2]
  return result

def calculate_distance_vector(pointA,pointB): #returns the vector that goes from point A to point B
  result=np.array([pointB[0]-pointA[0],pointB[1]-pointA[1]])
  return result

def calculate_distance(pointA,pointB): #returns the distance between point A and point B
  result=(((pointB[0]-pointA[0])**2)+((pointB[1]-pointA[1]])**2))**0.5
  return result

def label_to_point(label):
  return [label[6],label[7]]

def calcuate_center(labels): #set the center locations of all the given vehicles
  for i in labels:
    i[6],i[7]=calculate_label_center(i)
  return labels
                                                       
                                                     
  

def match_labels(oldlabels,labels): #matches the vehicles with the vehicles from the previous frame
  matchtable=np.array([])
  if(oldlabels.size=0):
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
  movement_vectors=np.zeros_like(matchtable,dtype=float)
  for i in range(matchtable.shape[0]):
    movement_vectors[i]=calculate_distance_vector(label_to_point(labels[matchtable[i,0]]),label_to_point(oldlabels[matchtable[i,1]]))
  return movement_vectors




def corolate(oldlabels,labels):
  if(oldlabels.size=0):
    pass
  else:
    pass

def run(source_path,weights_path):
  labels=np.array([])
  labelsold=np.array([])
  while(True):
    os.system(f"python detect.py --weights {weights_path} --source {source_path} --save-text --save-conf --nosave --line-thickness 1 --conf-thres 0.8")
    with open("runs/detect/exp/labels/image.txt","r") as f:
      if(labels.size==0):
        labelsold=np.array([])
      else:
        labelsold=deepcopy(labels)
      labels=np.asarray([i.split() for i in f.readlines()], dtype=float)
    labels=filters(labels,hwtreshold)
    labels=np.c_[labels, np.zeros(labels.shape[0]) , np.zeros(labels.shape[0])]
    labels=calcuate_center(labels)


if __name__ == "__main__":
  weights="Vehicle-Detection/runs/train/exp12/weights/best.pt"
  source="image.jpg"
  
  
