# coding=UTF-8
'''
Created on 2017年10月11日
@author: maksim-ssd
'''
from pybrain.tools.xml.networkreader import NetworkReader

# import skann as sn;
# net = NetworkReader.readFrom('../net/kdx_15l_100t.xml')

def dec2int(x):
    if x >= 0.5:
        return 1;
    elif x >= 0:
        return 0;
    else:
        return -1;
    
    
def isCorrect(arr,x):
    print(arr)
    if dec2int(arr[0]) == 0 and dec2int(arr[1]) == 0 and x == 0:
        return 1;
    elif dec2int(arr[0]) == 0 and dec2int(arr[1]) == 1 and x == 1:
        return 1;
    elif dec2int(arr[0]) == 1 and dec2int(arr[1]) == 0 and x == 2:
        return 1;
    elif dec2int(arr[0]) == 1 and dec2int(arr[1]) == 1 and x == 3:
        return 1;
    else:
        return 0;

def calRightRate(dataset,net):
    count = 0;
    for line in dataset:
        li = [];
        for i in range(len(line)-1):
            li.append(line[i]);
        if isCorrect(net.activate(li), line[-1]) == 1:
            count += 1;
    return float(count)/len(dataset);


# print(calRightRate(sn.gyvdataset,net));