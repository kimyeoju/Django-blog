from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm
from django.db.models import Q


# 글 목록 조회
class Index(View):
    def get(self, request):
        post = Post.objects.all()
        # Post 모델에서 전체 객체 가져오기
        context = {
            'posts': post,
            'title': 'Blog'
        }
        return render(request, 'blog/post_list.html', context)


# 글 작성
class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context ={
            'form': form,
            'title': 'Blog'
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        context = {
            'form' : form
        }
        return render(request, 'blog/post_form.html', context)


# 글 상세 조회
class DetailView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        # detail 객체 id=post_id로 선언
        context = {
            'title': 'Blog',
            'id': post_id,
            # 템플릿 안에서는 id라는 변수로 사용
            'post_writer': post.writer,
            'post_title': post.title,
            'post_content': post.content,
            'post_created_at': post.created_at
        }
        return render(request, 'blog/post_detail.html', context)
        

# 글 수정
class Update(View):
    def get(self,request, post_id):
        post = get_object_or_404(Post, id=post_id)
        # 조건을 만족하는 object가 있으면 해당 object를 리턴하고, 없으면 404처리 첫번째 인자 Post에서 두번째 인자 해당 아이디의 post객체를 가져오는 것 
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post,
            # post객체 값을 넘겨주어야 더 정확함
            'title':'Blog'
        }
        return render(request, 'blog/post_edit.html',context)
    
    def post(self,request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST)
        
        if form.is_valid():
            # 폼의 입력값을 얻고 싶은 경우는 form.cleaned_data
            # form.cleaned_data로 접근하면 폼 인스턴스 내에서 clean함수를 통해 변환되었을 수도 있는 데이터를 가져오므로 좋은 접근
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', post_id=post_id)
            # DetailView.get(self,request,post_id)로 정의했기 때문에 post_id로 attribute 선언해야함
        
        context = {
            'form': form,
            'title': 'Blog'
        }
        return render(request, 'blog/post_edit.html', context)


# 글 삭제
class Delete(View):
    def post(self,request,post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return redirect('blog:list')
    

# 글 검색
class SearchList(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
        context = {
            'search_query': search_query,
            'posts': posts
        }
        return render(request, 'blog/post_list.html', context)

        