# coding=UTF-8
'''
Created on 2017年10月21日
@author: maksim-ssd
程序入口
'''
import datetime
import os.path

from v2.datafileoperate import t1
from v2.download import download
from v2.drawpic import drawPic
from v2.secondtraining import t3
from v2.skann import t2


#所有股票的训练range是向前的天数
def eeveryStockTg(stock,sdateb,stdatee,range):
    if os.path.isdir("../"+stock+"/"):
        pass;
    else:
        os.mkdir("../"+stock+"/");
        os.mkdir("../"+stock+"/combine");
        os.mkdir("../"+stock+"/nets");
        os.mkdir("../"+stock+"/result");
    download(stock,sdateb,stdatee,"../"+stock+"/");
    download("000001",sdateb,stdatee,"../"+stock+"/");
    
    t1("../"+stock+"/", "000001", stock, range, "r"+str(range));
    t2("../"+stock+"/","r"+str(range));
    return;

#每天每股预测,大于rate的参与预测
def eeveryStockPrt(stock,range,rate):
    path = "../"+stock+"/";
    prt = t3(path,"r"+str(range),"r"+str(range)+"_8l_100t_"+str(rate));
    output = open(path+"result/res.txt", 'a')
    output.write(str(datetime.datetime.now().month)+"月"+str(datetime.datetime.now().day)+"日: "+str(prt)+"\n")
    output.close( )
    return;

############合并的步骤#######################
slist = ["002450","601899","000063","601218"];
for ele in slist:
    eeveryStockTg(ele,"20160120","20171020",70);

# for ele in slist:
#     eeveryStockPrt(ele,70,0.69);


######################分开的步骤########################
# download("002450","20170120","20171020","../datav6/");
# download("0000001","20170120","20171020","../datav6/");
# t1("../datav5/", "000001", "601899", 1000, "r1000");
# drawPic("../datav5/combine/r1000");
# t2("../datav4/","r100");
# t3("../datav4/","r100","r100_8l_100t_0.631578947368");
################################################