from django.conf.urls import url
from . import views

app_name = "booktest"

urlpatterns = [
    url(r'^index/$',views.index,name="index"),
    # url(r'^detail/$',views.detail)
    url(r'^list/$',views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name="detail"),
    url(r'^delete/(\d+)/$',views.delete,name="delete"),
    url(r'^addHero/(\d+)/$',views.addHero,name="addHero"),
    url(r'^addherotool/(\d+)$',views.addherotool,name="addherotool")
]