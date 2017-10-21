# coding=UTF-8
'''
Created on 2017年10月21日
@author: maksim-ssd
程序入口
'''

from v2.datafileoperate import t1
from v2.drawpic import drawPic
from v2.secondtraining import t3
from v2.skann import t2


t1("../datav4/", "000001", "002450", 100, "r100");
drawPic("../datav4/combine/r100");
# t2("../datav3/","r60");
# t3("../datav3/combine/r60", "../datav3/nets/8l_100t_rate_0.636363636364");