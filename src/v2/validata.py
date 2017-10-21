# coding=UTF-8
'''
Created on 2017年10月16日
@author: maksim-ssd
'''

#神经输出结果化为-1,0,1
def dec2int(x):
    if x <= -1.0/3:
        return -1;
    elif x <= 1.0/3:
        return 0;
    elif x <= 1:
        return 1;
    
#计算正确率
def calRightRate(dataset,net):
    count = 0;
    for line in dataset:
        li = [];
        for i in range(len(line)-1):
            li.append(line[i]);
        if dec2int(net.activate(li)) == line[-1]:
            count += 1;
#         print(line," $ ",dec2int(net.activate(li)));
    return float(count)/len(dataset);