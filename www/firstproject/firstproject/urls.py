from django.urls import re_path as url
from django.urls import include,path

from django.contrib import admin

from stockapp.views import * 
from mysite import views as mysiteViews

myUrlPatterns=[
    path('/',mysiteViews.homePage),

    path('/datatable',mysiteViews.datatable,name='datatable'),
    path('/stockChart',mysiteViews.stockChart,name='stockChart')
]
urlpatterns = [
    #test data only
    #======= stock app ============
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^$', home),
    url(r'^add/(\w+)/(\w+)/$', myAdd),
    url(r'^add2/(\w+)/(\w+)/$', myAdd2),
    url(r'^udn_query/$', udn_query),
    url(r'^stockListQuery/$', stockListQuery),
    url(r'^stockIdQuery/(\w+)/$', stockIdQuery), #GET
    url(r'^stockIdQuery/$', stockIdQuery), #POST
    
    url(r'^test/$', test),   
    path('mysite',include(myUrlPatterns)),
]
