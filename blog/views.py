from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, BlogComment, Tag, Suggest
from .forms import BlogCommentForm, SuggestForm,ArticleForm


def cover(request):
    aform = ArticleForm()
    
    return render(request,'home.html',{'aform':aform})

def home(request):
    article = Article.objects.all()
    cform = BlogCommentForm()
    aform = ArticleForm()
    return render(request,'article.html',{'article':article,'comment':cform,'aform':aform})


# Create your views here.
