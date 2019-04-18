from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Bookinfo,HeroInfo
from django.template import loader

# Create your views here.


def index(request):
    # return HttpResponse("首页")
    # temp = loader.get_template('booktest/index.html')
    # cont = {'username':'wangshuo'}
    # result = temp.render(cont)
    # return HttpResponse(result)
    #渲染
    return render(request,'booktest/index.html',{'username':'wangshuo'})


def list(request):
    # try:
    #     book = Bookinfo.objects.all()
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse("没有图书")
    book = Bookinfo.objects.all()
    return render(request,'booktest/list.html',{'booklist':book})


# def detail(request):
#     return HttpResponse("详情页")
def detail(request,i):
    # try:
    #     book = Bookinfo.objects.get(pk = int(i))
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse("没有此书")
    book = Bookinfo.objects.get(pk=int(i))
    return render(request,'booktest/detail.html',{'book':book})

def delete(request,i):
    try:
        Bookinfo.objects.get(pk = int(i)).delete()
        book = Bookinfo.objects.all()
        #渲染
        # return render(request, 'booktest/list.html', {'booklist': book})
        #重定向
        return HttpResponseRedirect("/list/",{'booklist': book})
    except:
        return HttpResponse("删除失败")

def addHero(request,i):
    book = Bookinfo.objects.get(pk=int(i))
    return render(request,'booktest/addhero.html', {'book': book})

def addherotool(request,i):
    book = Bookinfo.objects.get(pk=int(i))
    hname = request.POST['hname']
    res = request.POST['sex']
    if res == 1:
        hgender = True
    else:
        hgender = False
    hcontent = request.POST['hcontent']

    h = HeroInfo()
    h.hname = hname
    h.hgender = hgender
    h.hcontent = hcontent
    h.hBook = book
    h.save()
    return HttpResponseRedirect('/detail/'+str(i)+'/',{'book': book})

    # print(hname,hgender,hcontent,hBook_id)
    # return HttpResponse("添加成功")
