# coding=UTF-8
'''
Created on 2017年10月15日
@author: maksim-ssd
'''
import matplotlib.pyplot as plt
import numpy as np;
from v2.datafileoperate import getSp, calStatusLab, readFromCsv

def drawPic(ssp,status):
    a = np.arange(len(ssp)).reshape(len(ssp), 1)
    #绘图源数据
    res = np.hstack((a,ssp,status));
    
    x0 = [];
    x1 = [];
    x2 = [];
    
    y0 = [];
    y1 = [];
    y2 = [];
#     print(res);
    
    for line in res:
        if line[2] == -1:
            x0.append(line[0]);
            y0.append(line[1]);
        elif line[2] == 0:
            x1.append(line[0]);
            y1.append(line[1]);
        elif line[2] == 1:
            x2.append(line[0]);
            y2.append(line[1]);
    
    # x = np.arange(1,430,1);
    plt.title("I'm a scatter diagram.")
    plt.xlim(xmax=len(ssp)+3,xmin=0)
    plt.ylim(ymax=max(ssp)+3,ymin=min(ssp)-3)
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.plot(x,ssp,'r.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    
    plt.plot(x0,y0,'g.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.plot(x1,y1,'b.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.plot(x2,y2,'r.')#此处的r.的意思是red红色的.来绘图  r+  就是用红色的+来绘图
    plt.show()
    return;

cb = readFromCsv("../datav3/","cbf2");
drawPic(getSp(cb),calStatusLab(cb));