from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookinfo
from django.template import loader

# Create your views here.


def index(request):
    # return HttpResponse("首页")
    # temp = loader.get_template('booktest/index.html')
    # cont = {'username':'wangshuo'}
    # result = temp.render(cont)
    # return HttpResponse(result)
    return render(request,'booktest/index.html',{'username':'wangshuo'})


# def detail(request):
#     return HttpResponse("详情页")
def detail(request,i):
    # try:
    #     book = Bookinfo.objects.get(pk = int(i))
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse("没有此书")
    book = Bookinfo.objects.get(pk=int(i))
    return render(request,'booktest/detail.html',{'bookinfo':book})


def list(request):
    # try:
    #     book = Bookinfo.objects.all()
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse("没有图书")
    book = Bookinfo.objects.all()
    return render(request,'booktest/list.html',{'booklist':book})

def delete(request,i):
    try:
        Bookinfo.objects.get(pk = int(i)).delete()
        book = Bookinfo.objects.all()
        return render(request, 'booktest/list.html', {'booklist': book})
    except:
        return HttpResponse("删除失败")