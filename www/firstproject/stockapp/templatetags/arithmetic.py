from django import template
import pymysql 

register = template.Library()

@register.filter
def get_mod(arg1,arg2):
    value=int(arg1) % int(arg2)
    return value
    
@register.filter
def get_multi(arg1,arg2):
    value=arg1 * int(arg2)
    return value    
    
@register.filter
def get_divide(arg1,arg2):
    value=round(arg1 / float(arg2),2)
    string="%5.2f"%(value)
    return string
    
@register.filter
def str_concat(arg1,arg2):
    value=str(arg1)+str(arg2)
    return value    
    
@register.filter
def date2str(arg1,arg2):
    value=str(arg1)
    return value   

@register.filter
def  code2name(arg1,arg2):
    db = pymysql.connect(host="127.0.0.1", user="hsf",passwd="12345",database="stock",charset='utf8')
    cursor = db.cursor() 

    cmd="select name from stock_code_name where no='{}'".format(arg1)
    cursor.execute(cmd)
    db.commit()

    name=cursor.fetchone()[0]
    db.close()

    return name    