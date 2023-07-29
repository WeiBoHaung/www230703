from django.shortcuts import render


from stockapp.views import getStockListQuery,getStockDailyExchange
# Create your views here.

def homePage(request):
    '''
    http://127.0.0.1:8000/mysite/    會呼叫的這個function
    沒有做任何的動作回傳index.html
    '''
    return render(request,'mysite/index.html')
    
def datatable(request):
    '''
    http://127.0.0.1:8000/mysite/datatable    會呼叫的這個function
    '''
    allStockData=getStockListQuery()
    content={
        'allStockData':allStockData,
    }
    return render(request,'mysite/datatable.html',content)

def stockChart(request):
    '''
    http://127.0.0.1:8000/mysite/stockChart    會呼叫的這個function
    '''
    stockID=request.POST.get('stockID','')
    stockData=''
    if stockID != '':
        stockData=getStockDailyExchange(stockID)
        
    content={
        'stockID':stockID,
        'stockData':stockData
    }
    return render(request,'mysite/stockChart.html',content)