# coding=UTF-8
'''
Created on 2017年10月10日
@author: maksim-ssd
'''
import numpy as np;
import math as mh;
def readFromCsv(fname):
    myfile = open("../data/"+fname+".csv");
    return np.loadtxt(myfile,str,delimiter="," ,skiprows=0)

def write2CsvLine(fname,cont):
    myfile = open(r"../data/"+fname+".csv",'w');
    for line in cont:
        stmp="";
        for ele in line:
            stmp = stmp + ele + ",";
        #删除末尾的，要不再次导入数据的时候末尾的,后会被认为是一列特征，string - > float会失败
        stmp = stmp[:-1];
        myfile.writelines(stmp+"\n");
    myfile.close();
    return;

#给比较大的大盘成交金额每个数据都除以了10^11，要不没法处理
def sci2Float(sci):
    arr = sci.split("e+");
    print(arr);
    f = float(arr[0]) * 10 ** int(arr[1])/(10**int(arr[1]));
    return f;
#将成交额字段的所有信息转换为float
def sci2FloatList(slist):
    res = np.zeros((len(slist),1));
    for i in range(len(slist)):
        res[i][0] = sci2Float(slist[i][0]);
    return res;

#获得两个文件的合并数据
def combineFile():
    dapan = readFromCsv("000001");
    stock = readFromCsv("002450");
    #时间    后面的[::-1]是为了倒序，因为下载的时间时由近到远的
    sdate = dapan[1:,0:1][::-1];
    #大盘收盘价
    dsp = dapan[1:,3:4][::-1];
    #大盘最高价
    dmxp = dapan[1:,4:5][::-1];
    #大盘最低价
    dmnp = dapan[1:,5:6][::-1];
    #大盘开盘价
    dkp = dapan[1:,6:7][::-1];
    #大盘成交量
    dcjl = dapan[1:,10:11][::-1];
    #大盘成交额
    dcje = dapan[1:,11:12][::-1];
    dcje = sci2FloatList(dcje);
    #个股收盘
    ssp = stock[1:,3:4][::-1];
    #个股最高价
    smxp = stock[1:,4:5][::-1];
    #个股的最低价
    smnp = stock[1:,5:6][::-1];
    #个股的开盘价
    skp = stock[1:,6:7][::-1];
    #换手率
    shsl = stock[1:,7:8][::-1];
    #成交量
    scjl = stock[1:,8:9][::-1];
    #成交额
    scje = stock[1:,9:10][::-1];
    #总市值
    szsj = stock[1:,10:11][::-1];
    #流通市值
    sltsz = stock[1:,11:12][::-1];
    res = np.hstack((dsp,dmxp,dmnp,dkp,dcjl,dcje,ssp,smxp,smnp,skp,shsl,scjl,scje,szsj,sltsz))
    #停盘的将那些天删除
#     print(np.shape(res));
    return res;

#合并个股+大盘+当天的状态标志
def combineFileAStatue(cb):
    status = calStatus(cb);
    return np.hstack((cb,status));

#根据收盘价计算极值以及单调性
def calStatus(cb):
    cb = np.array(cb,dtype=np.float64);
    ssp = cb[:,6:7];
    status = np.zeros((len(ssp),1));
#     status = [];
    #前后15天
    radius = 15;
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
            return 0;#极小值
    elif l < p and r < p:
            return 1;#极大值
    elif l <= p <= r:
            return 2;#递增
    elif l >= p >= r:
            return 3;#递减
    else:
        return -1;

#得到收盘价格
def getSp(cb):
    cb = np.array(cb,dtype=np.float64);
    ssp = cb[:,6:7];
    return ssp;
    


cb = combineFile();
# cbf = combineFileAStatue(cb);
# write2CsvLine("cbf",cbf);
