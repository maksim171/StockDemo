# coding=UTF-8
'''
Created on 2017年10月16日
@author: maksim-ssd
神经网络
'''
from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.structure.modules.tanhlayer import TanhLayer
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.xml.networkwriter import NetworkWriter
from sklearn import preprocessing
import validata as va;

import numpy as np;
from v2.datafileoperate import readFromCsv


#把数据集按照 8:2  分为训练和验证以及最后的今天要预测的数据
def dataSplit(dataset):
    datasize = len(dataset);
    trainingsize = int(datasize*0.8);
    print("split args:",datasize,trainingsize,datasize-trainingsize-1,1);
    r1 = dataset[:trainingsize,:];
    r2 = dataset[trainingsize:-1,:];
    r3 = dataset[-1:,:];
    return r1,r2,r3;

#所有的归一
def gyData(dataset):
    gy = dataset[:,:-1];
    X_scaled = preprocessing.scale(gy)
    gydataset = np.hstack((X_scaled,dataset[:,-1:]));
    return gydataset,gy.mean(axis=0),gy.std(axis=0);

#这里的inputs是矩阵不是列表,可以输入多行原始数据计算多个样本的特征
def calFeature(inputs,dmean,dstd):
    #出去最后的标签
    finput = inputs[:,:-1];
    labs = inputs[:,-1:];
    rows = np.shape(finput)[0];
    cols = np.shape(finput)[1];
    arr = np.zeros((rows,cols));
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = (finput[i][j] - dmean[j])/dstd[j];

    return np.hstack((arr,labs));

#从原始数据得到训练数据
def buildTrainingSet(gydataset):
    #最后的训练数据
    trainingset = SupervisedDataSet(15, 1);
    for line in gydataset:
        trainingset.addSample((line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14]), line[15]);
    return trainingset;


#路径，合并文件名
def t2(cepath,fname):
    cbf = readFromCsv(cepath + "combine/" + fname);
    numdataset = np.array(cbf,dtype=np.float64);
    #训练数据，验证数据，今天的数据
    tgdataset,vadataset,tydata = dataSplit(numdataset);
    #归一的参数
    gydata,dmean,dstd = gyData(tgdataset);
    
    #验证和今天的数据
    gyvadata = calFeature(vadataset,dmean,dstd);
    gytydata = calFeature(tydata,dmean,dstd);
    
    #神经网络
    trainingset = buildTrainingSet(gydata);
    
    for i in range(1000):
        net = buildNetwork(15, 8, 1, bias=True,hiddenclass=TanhLayer,outclass=TanhLayer)
        trainer = BackpropTrainer(net, trainingset)
        trainer.trainEpochs(epochs=100);
        rate = va.calRightRate(gyvadata,net);
        if rate > 0.6:
            NetworkWriter.writeToFile(net, cepath + 'nets/' + fname +'_8l_100t_'+str(rate)+".xml")
            print("current best rate: " + str(rate));
        else:
            print(str(i)+" times rate = "+ str(rate));

# t2("../datav3/","r20")