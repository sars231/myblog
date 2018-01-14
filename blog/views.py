from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, BlogComment, Tag, Suggest
from .forms import BlogCommentForm, SuggestForm


def cover(request):
    return render(request,'cover.html')

def home(request):
    article = Article.objects.all()
    return render(request,'article.html',{'article':article,})


# Create your views here.
