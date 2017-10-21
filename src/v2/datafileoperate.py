# coding=UTF-8
'''
Created on 2017年10月15日
@author: maksim-ssd
作用作为数据从文件读入和读出
'''
import numpy as np;

#读入  ../datav3/
def readFromCsv(path,fname):
    myfile = open(path + fname+".csv");
    return np.loadtxt(myfile,str,delimiter="," ,skiprows=0);

def write2CsvLine(path,fname,cont):
    myfile = open(path+fname+".csv",'w');
    for line in cont:
        stmp="";
        for ele in line:
            stmp = stmp + ele + ",";
        #删除末尾的，要不再次导入数据的时候末尾的,后会被认为是一列特征，string - > float会失败
        stmp = stmp[:-1];
        myfile.writelines(stmp+"\n");
    myfile.close();
    return;

#写入文件，返回内容
def combineFile(path,f1,f2):
    f1 = readFromCsv(path,f1);
    f2 = readFromCsv(path,f2);
    arr = np.hstack((f1,f2));
    #时间倒序
    arr = arr[::-1]
    #删除出现None的行
    #删除行的行号
    rows = np.shape(arr)[0];
    cols = np.shape(arr)[1];
    delrowls = [];
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == "None":
                delrowls.append(i);
                break;
    write2CsvLine(path,"cbf1",arr);
    #删除None的行数和最后一行标签行
    arr = np.delete(arr, delrowls, 0);
    arr = np.delete(arr,len(arr)-1,0);
    #删除不要的特征列
    arr = np.delete(arr,[0,1,2,7,8,9,12,13,14,19,20,21],1);
#     print(arr);
    return arr;


#sl左边序列  sr右边序列 p比较的数字  0极小值  1极大值 2递增 3递减
def getStatus(sl,sr,p):
    l = 0;
    r = 0;
    if len(sl)!=0 and len(sr)!=0:
        l = sum(sl)/len(sl);
        r = sum(sr)/len(sr);
    else:
        if len(sl) == 0:
            l = p;
            r = sum(sr)/len(sr); 
        else:
            l = sum(sl)/len(sl);
            r = p;
    if l > p and r > p:
            return -1;#极小值
    elif l < p and r < p:
            return 1;#极大值
    else:
        return 0;



#根据 收盘价 计算极值以及单调性
def calStatusLab(cb):
    cb = np.array(cb,dtype=np.float64);
    #收盘价ssp，作为标签计算依据
    ssp = cb[:,6:7];
    status = np.zeros((len(ssp),1));
    #求均值前后参考的天数，越大越接近全局值，如果操作周期为1个月建议设置成10天
    radius = 5;
    for i in range(len(ssp)):
        if (i-radius) > -1 and (i+radius) < len(ssp):
            l = ssp[i-radius:i-1];
            r = ssp[i+1:i+radius];
            p = ssp[i];
            status[i][0] = (getStatus(l,r,p));
        elif (i-radius) < 0:
            l = ssp[0:i];
            r = ssp[i+1:i+radius];
            p = ssp[i];
            status[i][0] = (getStatus(l,r,p));
        elif (i+radius) > len(ssp)-1:
            l = ssp[i-radius:i-1];
            r = ssp[i+1:len(ssp)-1];
            p = ssp[i];
            status[i][0] = (getStatus(l,r,p));
#     print(status);
    return status;

#得到收盘价格
def getSp(cb):
    cb = np.array(cb,dtype=np.float64);
    ssp = cb[:,6:7];
    return ssp;

#截取原始数据中向前range天的数据，因为有时短期的数据更加合适，长期的数据不具有训练价值
def rangeDDate(totoaldata,range):
    return totoaldata[:range,:];




cbf = combineFile("../datav3/","000001","000063");
#前90天作为训练样本
rdd = rangeDDate(cbf,30);
labs = calStatusLab(rdd);
cbf2 = np.hstack((rdd,labs));
write2CsvLine("../datav3/","cbf2",cbf2);
