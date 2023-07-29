from django.shortcuts import render  
from django.http import HttpResponse 
from django.shortcuts import redirect
from datetime import datetime
import json
import requests
import pymysql 
import numpy as np

def stockIdQuery(r,stockId=""):
    if r.method=="GET"  :
        db = pymysql.connect(host="127.0.0.1", user="hsf",passwd="12345",database="stock",charset='utf8')
        cursor = db.cursor() 

        cmd="select * from stock_code_name where no='{}'".format(stockId)
        cursor.execute(cmd)
        db.commit()
        
        data=cursor.fetchall()[0]
        
        db.close()
        return render(r,"stock/stockIdQueryDate.html",{'no':data[1],'name':data[2]}) 
        
    else: #method==POST
        #處理程序等下再寫
        db = pymysql.connect(host="127.0.0.1", user="hsf",passwd="12345",database="stock",charset='utf8')
        cursor = db.cursor() 
        
        no=r.POST.get('no')
        startDate=r.POST.get('startDate')
        endDate=r.POST.get('endDate')
 
        cmd="select * from stock_daily_exchange where no='{}' and date >='{}' and date <='{}'".\
            format(no,startDate,endDate)

        cursor.execute(cmd)
        db.commit()
        data=cursor.fetchall()
        db.close()
        
        # data=np.array(data)
        # for i in range(data.shape[0]):
            # data[i,1]=str(data[i,1])
        
        # tmp=[]
        # for i in data:
            # tmp.append(list(i))
        # data=tmp   
        return render(r,"stock/stockIdQueryResult.html",{"data":data})


def test(r):
    return render(r,"stock/test.html",{})
    
def stockListQuery(r):
    db = pymysql.connect(host="127.0.0.1", user="hsf",passwd="12345",database="stock",charset='utf8')
    cursor = db.cursor() 

    cmd="select `id`,`no`,`name`,`class` from stock_code_name"
    cursor.execute(cmd)
    data=cursor.fetchall()
    db.commit()

    db.close()
    return render(r,"stock/stockListQuery.html",{'data':data})
    
def index(r):
    return HttpResponse("<h1>hihi mary</h1>")
    
def home(r):
    return HttpResponse("<h1>這是首頁</h1>") 
    
def myAdd(r,x=0,y=0):
    z=int(x)+int(y)
    return HttpResponse(str(z))        
    
def myAdd2(r,x=0,y=0):
    z=(int(x)+int(y))/2
    return render(r,"stock/myadd2.html",{'first':x,'second':y,'ave':z})    

def udn_query(r):
    if r.method=="GET"  :
         return render(r,"stock/udn_query.html",{}) 
    else: #method==POST
        keyword=r.POST.get('key')
        if keyword != None:
            url="https://udn.com/api/more?page=2&id=search:{}&channelId=2&type=searchword&last_page=1777".format(keyword)
            data=requests.get(url).text
            data=json.loads(data)

            news=[]

            for i in range(len(data['lists'])):
                title=data['lists'][i]['title']
                url=data['lists'][i]['titleLink']
                date=data['lists'][i]['time']['date'][:10]
                news.append({'title':title,'url':url,'date':date})
            return render(r,"stock/udnNewsList.htm",{'news':news})
        else:
            return HttpResponse("<h1>pass</h1>")

def getStockListQuery():
    '''
    取得股市列表類別
    '''
    db = pymysql.connect(host="127.0.0.1", user="hsf",passwd="12345",database="stock",charset='utf8')
    cursor = db.cursor() 

    cmd="select * from stock_code_name"
    cursor.execute(cmd)
    data=cursor.fetchall()
    db.commit()

    db.close()
    return data

def getStockDailyExchange(no):
    '''
    取得股市所有資料
    '''
    db = pymysql.connect(host="127.0.0.1", user="hsf",passwd="12345",database="stock",charset='utf8')
    cursor = db.cursor() 
    
    cmd="select *, DATE_FORMAT(date, '%Y-%m-%d') AS date_str from stock_daily_exchange where no='{}'".format(no)

    cursor.execute(cmd)
    db.commit()
    results_tuples =cursor.fetchall()
    db.close()
    # tuple轉字典
    results_list = list(map(lambda row: {"date": row[8], "open": row[3],"high": row[4],"low": row[4],"close": row[5] }, results_tuples))
    # 把日期字串轉毫秒
    for price in results_list:
        dt_object = datetime.strptime(price['date'], '%Y-%m-%d')
        price['date']= int(dt_object.timestamp() * 1000)

    return results_list