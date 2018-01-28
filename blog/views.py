from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article, Category, BlogComment, Tag, Suggest
from .forms import BlogCommentForm,SuggestForm,ArticleForm,TagForm


def cover(request):
    aform = Article.objects.all()
    
    return render(request,'home.html',{'aform':aform})

@login_required(login_url='/admin/login')
def edit(request):
    if request.method == 'GET':
        edit_form = ArticleForm()
        tag_form = TagForm()
        return render(request,'edit_blog.html',{'edit_form':edit_form,'tag_form':tag_form})
    elif request.method == 'POST':
        edit_form = ArticleForm(request.POST)
        
        edit_form.save()
        return redirect('/')
    

# Create your views here.
