# coding=UTF-8
'''
Created on 2017年10月21日
@author: maksim-ssd
'''
import requests as rs;

#下载sid股票id，起止时间，url,位置
def download(sid,sdateb,sdatee,path):
    if sid == "000001":
        strs = "http://quotes.money.163.com/service/chddata.html?code=0000001&start="+sdateb+"&end="+sdatee+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER"
    else:
        if sid[0] == "0":
            strs = "http://quotes.money.163.com/service/chddata.html?code="+"1"+sid+"&start="+sdateb+"&end="+sdatee+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP";
        else:    
            strs = "http://quotes.money.163.com/service/chddata.html?code="+sid+"&start="+sdateb+"&end="+sdatee+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP";
#     print(strs);
    r = rs.get(strs);
    with open(path + sid+".csv", "wb") as code:
        code.write(r.content)
    return;

# download("0600795","20170120","20171020","../dd/");
# download("0000001","20170120","20171020","../dd/");
