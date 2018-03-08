"""
Created on Fri Mar 02 18:28:30 2018

@author: bedro
"""
from __future__ import division
import matplotlib.pyplot as mp
import numpy as np #imports NumPy
import os
from PIL import Image

#from PIL import ImageFilter

#
imlist = []

#scanning images from directory
path = './rebelmrkt/'
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.jpg'):
            try:
                
                img = Image.open(path+file)
                img = np.float32(img)
                imlist.append(img)
#                mp.imshow(img)
#                mp.show()
            except (IOError, SyntaxError) as e:
                print('Bad file:', file)
                
#averaging image out
avg_img=imlist[0]
for index in range(1, len(imlist)):
    avg_img+=imlist[index]
avg_img/=len(imlist)


#finding standard deviation
std=[0,0,0]
for img in imlist:
    std+=(img-avg_img)**2
std = np.sqrt(std/(len(imlist)-1))


#asking threshold and highlitting the area
n = raw_input('Enter minimum threshold value? \n')
for i in range(0,len(std)):
    for j in range(0,len(std[0])):
        if (std[i][j] > int(n)).any():
            avg_img[i][j] = [255,0,0]
avg_img = np.uint8(avg_img)

#printing image
mp.imshow(avg_img)

#saving the plot and printing it
mp.savefig('Threshhold-40.jpg')
mp.show()



