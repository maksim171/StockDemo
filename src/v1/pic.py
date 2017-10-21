# coding=UTF-8
'''
Created on 2017年10月9日

@author: maksim-ssd
'''

import matplotlib.pyplot as plt
import numpy as np;
from v1.util import combineFile, calStatus, getSp


def drawPic():
    cf = combineFile();
    ssp = getSp(cf);
    status = calStatus(cf);
    a = np.arange(len(ssp)).reshape(len(ssp), 1)
    #绘图源数据
    res = np.hstack((a,ssp,status));
    
    x0 = [];
    x1 = [];
    x2 = [];
    x3 = [];
    y0 = [];
    y1 = [];
    y2 = [];
    y3 = [];
    print(res);
    
    for line in res:
        if line[2] == 0:
            x0.append(line[0]);
            y0.append(line[1]);
        elif line[2] == 1:
            x1.append(line[0]);
            y1.append(line[1]);
        elif line[2] == 2:
            x2.append(line[0]);
            y2.append(line[1]);
        elif line[2] == 3:
            x3.append(line[0]);
            y3.append(line[1]);
            
    
    # x = np.arange(1,430,1);
    plt.title("I'm a scatter diagram.")
    plt.xlim(xmax=430,xmin=0)
    plt.ylim(ymax=7,ymin=3)
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.plot(x,ssp,'r.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    
    plt.plot(x0,y0,'r.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.plot(x1,y1,'g.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.plot(x2,y2,'b.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.plot(x3,y3,'k.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    
    plt.show()
    return;

drawPic();