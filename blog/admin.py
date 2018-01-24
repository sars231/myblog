from django.contrib import admin
from .models import Article,Category,Tag,Suggest,BlogComment

# Register your models here.
admin.site.register([Article,Category,Tag,Suggest,BlogComment])

class Media:
    js = (
        '/static/js/kindeditor/kindeditor-min.js',
        '/static/js/kindeditor/lang/zh_CN.js',
        '/static/js/kindeditor/config.js',
    )