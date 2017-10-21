# coding=UTF-8
'''
Created on 2017年10月12日
@author: maksim-ssd
'''
from pybrain.tools.xml.networkreader import NetworkReader
import skann as sn;

net = NetworkReader.readFrom('../net/testNet_6l_100t.xml');
ll = [3382.9879,3384.0262,3358.7953,3373.3446,179423841,2.31148615058,4.4,4.4,4.35,4.36,0.4556,4518585,19794038.0,4363744000.0,4363744000.0];
today = sn.calTodayFeature(ll,sn.trainingset);
print(net.activate(today));