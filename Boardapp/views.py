from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog
 

# Create your views here.

def welcome(request):
    return render(request, 'Boardapp/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'Boardapp/read.html', {'blogs':blogs})

def create(request):
    if request.method == 'POST': #1 새로운 글 저장 == POST
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect ('read')
    
    else:  #글쓰기 페이지 띄워주기 == GET
        form = NewBlog()
        return render(request, 'Boardapp/create.html', {'form':form})

def update(request,pk):
    blog = get_object_or_404(Blog, pk = pk) #어떤 블로그 수정할지 객체 가져오기
    form = NewBlog(request.POST, instance = blog) #해당 블로그 객체pk에 맞는 수정내용입력공간
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'Boardapp/create.html', {'form':form})

def delete(request,pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('read')