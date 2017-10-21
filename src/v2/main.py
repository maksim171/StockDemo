# coding=UTF-8
'''
Created on 2017年10月21日
@author: maksim-ssd
程序入口
'''

from v2.datafileoperate import t1
from v2.download import download
from v2.drawpic import drawPic
from v2.secondtraining import t3
from v2.skann import t2


download("0600795","20170120","20171020","../datav6/");
download("0000001","20170120","20171020","../datav6/");

# t1("../datav5/", "000001", "601899", 1000, "r1000");
# drawPic("../datav5/combine/r1000");
# t2("../datav4/","r100");
# t3("../datav4/combine/r100", "../datav4/nets/r100_8l_100t_0.631578947368");