from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Article
from .forms import PostForm,RegisterForm

# Create your views here.
def index(request):
    queryset = Article.objects.order_by('-id').select_related('author').all()
    pageobj = Paginator(queryset,9)
    page = request.GET.get('page')
    pagelist = pageobj.get_page(page)

    context = {
            # 'posts':queryset,
            'posts':pagelist
        }
    return render(request,'blog/index.html',context)

def post_detail(request,id):
    post = Article.objects.get(pk=id)
    context = {
        'post':post
    }

    return render(request,'blog/postdetail.html',context)

@login_required
def createpost(request):
    postform = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            thepost = form.save(commit=False)
            thepost.author = request.user
            thepost.save()
            return redirect('main_home')

    context = {
        'form':postform
    }

    return render(request,'blog/createpost.html',context)

def register(request):
    regForm = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':regForm
    }
    return render(request,'registration/register.html',context)