# coding=UTF-8
'''
Created on 2017年10月9日
@author: maksim-ssd
'''

from scipy.io.matlab.miobase import arr_dtype_number
from sklearn import preprocessing;

import numpy as np;


# from v1.util import sci2Float
li = [1,2,3,4];

arr = np.zeros((429,1));
arr[0][0] = 1;
arr[1][0] = 2;
arr[2][0] = 3;
arr[3][0] = 4;


# print(arr);
# print(np.shape(arr));

# strr = "2.13e+10"
# print strr.split("e+")

# print(sci2Float(strr));
f = 2.13;
print(round( f , 2 ));