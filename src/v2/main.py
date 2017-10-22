# coding=UTF-8
'''
Created on 2017年10月21日
@author: maksim-ssd
程序入口
'''
import os.path

from v2.datafileoperate import t1
from v2.download import download
from v2.drawpic import drawPic
from v2.secondtraining import t3
from v2.skann import t2


def eeveryStock(stock,sdateb,stdatee):
    if os.path.isdir("../"+stock+"/"):
        pass;
    else:
        os.mkdir("../"+stock+"/");
        os.mkdir("../"+stock+"/combine");
        os.mkdir("../"+stock+"/nets");
        os.mkdir("../"+stock+"/result");
    download(stock,sdateb,stdatee,"../"+stock+"/");
    download("000001",sdateb,stdatee,"../"+stock+"/");
    
    t1("../"+stock+"/", "000001", stock, 1000, "r1000");
    
    return;

# eeveryStock("002450","20170120","20171020");

download("002450","20170120","20171020","../datav6/");
# download("0000001","20170120","20171020","../datav6/");

# t1("../datav5/", "000001", "601899", 1000, "r1000");
# drawPic("../datav5/combine/r1000");
# t2("../datav4/","r100");
# t3("../datav4/","r100","r100_8l_100t_0.631578947368");