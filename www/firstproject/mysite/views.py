from django.shortcuts import render


from stockapp.views import getStockListQuery
# Create your views here.

def homePage(request):
    allStockData=getStockListQuery()
    content={
        'allStockData':allStockData,
    }
    return render(request,'mysite/index.html',content)