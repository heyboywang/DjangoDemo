from django.contrib import admin
from .models import Bookinfo,HeroInfo

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1



# Register your models here.
class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['btitle','bpub_date']
    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ['hname','hgender','skill']
    #过滤字段
    list_filter = ['hgender','hcontent']
    #搜索字段
    search_fields = ['hname','hgender','hcontent']
    #分页显示
    list_per_page = 3


admin.site.register(Bookinfo,BookinfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
