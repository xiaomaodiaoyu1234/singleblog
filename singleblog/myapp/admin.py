from django.contrib import admin
from .models import Post,Tag,Cagr
# Register your models here.
# admin.site.register(Post)
# @admin.register(Post)

class Post_online(admin.TabularInline):
    model = Post
    extra = 2



@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ['title','content','desc','myca','mytag','id']
    # fieldsets = (
    #     ('标题/正文', {'fields': ['title', 'content']}),
    #     ('分类/标签', {'fields': ['con', 'tag']}),
    # )
    search_fields = ['title', 'content', 'desc','con__cag_name']  # 添加搜索字段
    # list_filter = ['title', 'con','tag']
    list_filter = ['title','tag']
    fieldsets = [('标题/正文', {'fields': ['title', 'content']}),('分类/标签', {'fields': ['con', 'tag']}),]
    list_per_page = 2
# fieldsets = (
#     ('标题/正文',{'fields':['title','content']}),
#     ('分类/标签',{'fields':['con','tag']}),
# )
admin.site.register(Tag)
# admin.site.register(Cagr)
@admin.register(Cagr)
class Catadmin(admin.ModelAdmin):
    list_display = ['cag_name','id']
    inlines = [Post_online]

