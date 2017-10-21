# coding=UTF-8
'''
Created on 2017年10月20日
@author: maksim-ssd
二次训练，就是将验证数据放入网络再次训练
最后输出最终的预测结论
'''
import numpy as np;
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.tools.xml.networkreader import NetworkReader
from v2.datafileoperate import readFromCsv
from v2.skann import dataSplit, gyData, calFeature, buildTrainingSet
from v2.validata import dec2int


def t3(cbfpath,netpath):
    cbf = readFromCsv(cbfpath);
    numdataset = np.array(cbf,dtype=np.float64);
    #训练数据，验证数据，今天的数据
    tgdataset,vadataset,tydata = dataSplit(numdataset);
    #归一所有的文件中的数据
    '''
         此处与skann的处理有所不同，在skann中因为要将数据集分为训练数据集和验证数据集，所以在
    gyData时调用gyData(tgdataset)，而在二次训练时应该用全局的均值和方差来求隶属度，所以调用
    gyData时调用gyData(numdataset)
    '''
    gydata,dmean,dstd = gyData(numdataset);
    
    #验证和今天的数据
    gyvadata = calFeature(vadataset,dmean,dstd);
    gytydata = calFeature(tydata,dmean,dstd);
    
    tset = buildTrainingSet(gyvadata);
    
    net = NetworkReader.readFrom(netpath+".xml");
    trainer = BackpropTrainer(net, tset)
    trainer.trainEpochs(epochs=100);
    li = [];
    for ele in gytydata[0]:
        li.append(ele);
    print(dec2int(net.activate(li[:-1])))
    return;

#合并文件位置，神经网络位置
# t3("../datav3/combine/r20", "../datav3/nets/8l_100t_rate_0.666666666667");
