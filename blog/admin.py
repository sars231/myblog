from django.contrib import admin
from .models import Article,Category,Tag,Suggest,BlogComment

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','body','created_time','last_modified_time','status','abstract','views',
    'likes','topped','category')
admin.site.register(Article,ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_time','last_modified_time')
admin.site.register(Category,CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','created_time','last_modified_time')
admin.site.register(Tag,TagAdmin)

class SuggestAdmin(admin.ModelAdmin):
    list_display = ('suggest','suggest_time')
admin.site.register(Suggest,SuggestAdmin)

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','body','created_time','article')
admin.site.register(BlogComment,BlogCommentAdmin)

class Media:
    js = (
        '/static/js/kindeditor/kindeditor-min.js',
        '/static/js/kindeditor/lang/zh_CN.js',
        '/static/js/kindeditor/config.js',
    )