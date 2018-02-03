from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Article, Category, BlogComment, Tag, Suggest
from .forms import BlogCommentForm,SuggestForm,ArticleForm,TagForm,CategoryForm


def home(request):
    article_list = Article.objects.all()
    print(article_list)
    paginator = Paginator(article_list,2)
    page = request.GET.get('page')
    try:
        art = paginator.page(page)
    except PageNotAnInteger:
        art = paginator.page(1)
    except  EmptyPage:
        art = paginator.page(paginator.num_pages)   
    return render(request,'home.html',{'aform':art,})

@login_required(login_url='/admin/login')
def edit(request):
    if request.method == 'GET':
        edit_form = ArticleForm()
        tag_form = TagForm()
        cform = CategoryForm()
        return render(request,'edit_blog.html',{'edit_form':edit_form,'tag_form':tag_form,'cform':cform})
    elif request.method == 'POST':
        edit_form = ArticleForm(request.POST)
        cform = CategoryForm(request.POST)
        cform.save()
#        edit_form.save()
        return redirect('/')
    

# Create your views here.
