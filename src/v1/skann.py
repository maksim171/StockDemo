# coding=UTF-8
'''
Created on 2017年10月10日
@author: maksim-ssd
'''
from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.structure.modules.tanhlayer import TanhLayer
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkwriter import NetworkWriter
from sklearn import preprocessing

import numpy as np;
from v1.util import readFromCsv
import validate as ve;


#所有的归一
def gyData(dataset):
    gy = dataset[:,:-1];
    X_scaled = preprocessing.scale(gy)
    gydataset = np.hstack((X_scaled,dataset[:,-1:]));
    return gydataset;

#把数据集按照 8:2  分为训练和验证
def dataSplit(gydataset):
    datasize = len(gydataset);
    trainingsize = int(datasize*0.8);
    print(datasize,trainingsize,datasize-trainingsize);
    r1 = gydataset[:trainingsize,:];
    r2 = gydataset[trainingsize:,:];
    return r1,r2;


#从原始数据得到训练数据
def buildTrainingSet(dataset):
#     gy = dataset[:,:-1];
#     X_scaled = preprocessing.scale(gy)
#     gydataset = np.hstack((X_scaled,dataset[:,-1:]));
    gydataset = dataset;
#     print(gydataset[:,5:6]);
    #最后的训练数据
    trainingset = SupervisedDataSet(15, 2);
    for line in gydataset:
        if line[-1] == 0:
            trainingset.addSample((line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14]), (0,0));
        elif line[-1] == 1:
            trainingset.addSample((line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14]), (0,1));
        elif line[-1] == 2:
            trainingset.addSample((line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14]), (1,0));
        elif line[-1] == 3:
            trainingset.addSample((line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14]), (1,1));
    return trainingset;

#输入特征，输出标签，训练数据  srcdata  是不归一的数据
def calTodayFeature(inputs,srcdata):
    meanlist = srcdata.mean(axis=0);
    stdlist = srcdata.std(axis=0);
#     print(meanlist);
#     print(stdlist);
    ls = [];
    for i in range(len(inputs)):
        ls.append((inputs[i] - meanlist[i])/stdlist[i])
    return ls;



#读入字符串
dataset = readFromCsv("cbf");
#化为float
numdataset = np.array(dataset,dtype=np.float64);
#原始分割为两组
trainingset,vdataset = dataSplit(numdataset);
# print(len(trainingset),len(vdataset));
#分别归一化
gytdataset = gyData(trainingset);
gyvdataset = gyData(vdataset);




#下面的是训练神经网络

# #最终的训练集,用归一化的数据来构成训练集
bts = buildTrainingSet(gytdataset);
# ll = [3382.9879,3384.0262,3358.7953,3373.3446,179423841,2.31148615058,4.4,4.4,4.35,4.36,0.4556,4518585,19794038.0,4363744000.0,4363744000.0];
# print(calTodayFeature(ll,trainingset));
net = buildNetwork(15, 4, 2, bias=True,hiddenclass=SigmoidLayer,outclass=SigmoidLayer)
trainer = BackpropTrainer(net, bts)
trainer.trainEpochs(epochs=100);
NetworkWriter.writeToFile(net, '../net/jxkj_4l_100t.xml')
#

print(ve.calRightRate(gyvdataset,net));