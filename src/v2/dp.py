# coding=UTF-8
'''
Created on 2017年10月16日
@author: maksim-ssd
'''
import matplotlib.pyplot as plt
import numpy as np;

def drawPic(ssp):
    size = len(ssp);
    lx = range(0,size,1);
    ly = [];
    
    for i in range(size):
        ly.append(ssp[i][0]);
    
    print(np.shape(lx),np.shape(ly));
    print(lx);
    print(ly);
    # x = np.arange(1,430,1);
    plt.title("I'm a scatter diagram.")
    plt.xlim(xmax=size,xmin=0)
    plt.ylim(ymax=5,ymin=-5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(lx,ly,'r.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.show()
    return;

