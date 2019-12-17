## made by EthanJ

import sys
import os
from os import listdir
from PIL import Image
from os.path import isfile, isdir, join, dirname, splitext, basename
import json

Path = os.path.dirname(os.path.realpath(__file__))

def data_check(file, img_file):

    with open(file,'r') as f:
        pic_image_json = json.load(f)
    
    img_dir= "D://TobeMoved//images//"+ img_file + ".jpg"
    
    with open(img_dir,'rb') as img_id:
        img=Image.open(img_id)
        
    realwidth,realheight= img.size
        
    width = pic_image_json['imageWidth']
    height = pic_image_json['imageHeight']
    
    if(width!=realwidth):
        print(img_dir)
        print("Please Check img_size Width with the image size \n")
    elif (height!=realheight):
        print(img_dir)
        print("Please Check img_size height with the image size \n")
        
    xmin=''
    ymin=''
    xmax=''
    ymax=''
    objects = []
    json_shapes = pic_image_json["shapes"]
    for object in json_shapes:
        xmin=object["points"][0][0]
        ymin= object["points"][0][1]
        xmax=object["points"][1][0]
        ymax=object["points"][1][1]
        
        verify_obj(xmin,ymin,xmax,ymax,width,height)
        
        objects.append({
                    "name" : object["label"].lower(),
                    "xmin" : object["points"][0][0],
                    "ymin" : object["points"][0][1],
                    "xmax" : object["points"][1][0],
                    "ymax" : object["points"][1][1]
                })
    
    #print(objects)
def verify_obj(xmin,ymin,xmax,ymax,width,height):
    
    if(xmin>width or xmin<0):
        print(file + " has xmin error")
        print(xmin)
        print("max_width: " + str(width) + "\n")
    elif(xmax>width or xmax<0):
        print(file + " has xMax Error")
        print(xmax)
        print("max_width: " + str(width) + "\n")
    elif(ymin>height or ymin<0):
        print(file + " has ymin Error")
        print(ymin)
        print("max_height: " + str(height) + "\n")
    elif(ymax>height or ymax<0):
        print(file + " has Ymax Error")
        print(ymax)
        print("max_height: " + str(height) + "\n")
    #else:
        #print(file + " is Fine")


for root, dir, files in os.walk(Path):
        for file in files:
            if file.lower().endswith(".json"):
                file_name=file.upper().split(".")[0]
                data_check(os.path.join(root, file), file_name)
                
print("Done Checking OffCourse")
