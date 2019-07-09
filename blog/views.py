from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .form import NewBlog, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator
# 페이지네이션하귀 위해



# 어떤 데이터를 어떻게 처리할지 함수로 정의해야됨

def  home(request):
    # 홈이라는 함수를 선언한다 리퀘스트를 인자로 받는다.
    blogs = Blog.objects
    # 블로그의 객체를 블로그스에 담아준다

    blog_list = Blog.objects.all()
    # 블로그 객체를 세개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    # 해당페이지로 이동하는

    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

    # 쿼리셋과 메소드의 형식
    # 모델, 쿼리셋(objects).메소드



def new(request):
    return render(request, 'new.html')


def create(request):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST' :
        form = NewBlog(request.POST)
        
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('home')
    # 글쓰기 페이지를 띄워주는 역할 == GET
    else:
        form = NewBlog()
        return render(request, 'new.html', {'form':form})

#수정 함수
def update(request, pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    #해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance = blog)
    # 원래 써둔 객체를 불러와라 (instance = blog)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'new.html', {'form':form})

#삭제함수
def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form' : form})

def detail(request, pk):
    detail = get_object_or_404(Blog, pk = pk)
    return render(request, 'detail.html', {'details' : detail})
# 어떤 클래스, 검색조건(몇번데이터,pk)
# pk = primary key 객체들의 이름표, 구분자, 데이터의 대표값