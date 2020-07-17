# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:54:45 2020

@author: 91701
"""
import os
import cv2
import numpy as np

def load_dataset(path,mode,size=(64,64)):
    filenames=path
    cs=[]
    ca=os.listdir(filenames)
    img_w=size[0]
    img_h=size[1]
    count=-1
    x_train=list()
    for c in ca:
        count=count+1
        p=os.path.join(filenames,c)
        fi=os.listdir(p)
        for f in fi:
            try:
                path1=os.path.join(p,f)
                image=cv2.imread(path1)
                image=cv2.resize(image,(img_w,img_h))
                if mode=='gray':
                    image_f = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                if mode=='rgb':
                    image_f = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image_f=image_f/255
                x_train.append(image_f)
                cs.append(count)
            except:
                print("Bad Format")
    x_train=np.array(x_train)
    y_train=[cs]
    y_train=np.array(y_train)
    y_train=y_train.T

    shuffler = np.random.permutation(len(x_train))
    x = x_train[shuffler]
    y = y_train[shuffler]

    x=x.flatten().reshape(x.shape[1]*x.shape[2]*x.shape[3],x.shape[0])
    y=y.T
    return(x,y)



