from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from .forms import PostForm

# Create your views here.
class Index(View):
    def get(self, request):
        post = Post.objects.all()
        # Post 모델에서 전체 객체 가져오기
        context = {
            'posts': post,
            'title': 'Blog'
        }
        return render(request, 'blog/post_list.html', context)


class Write(View):
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
            post = form.save()
            return redirect('blog:list')


class DetailView(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        context = {
            'title': 'Blog',
            'post_id': post_id,
            'post_title': post.title,
            'post_content': post.content,
            'post_created_at': post.created_at
        }
        return render(request, 'blog/post_detail.html', context)
        


class Update(View):
    def get(self,request, post_id):
        post = get_object_or_404(Post, pk=post_id)
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
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST)
        if form.is_valid():
            # 폼의 입력값을 얻고 싶은 경우는 form.cleaned_data
            # form.cleaned_data로 접근하면 폼 인스턴스 내에서 clean함수를 통해 변환되었을 수도 있는 데이터를 가져오므로 좋은 접근
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=post_id)
        
        context = {
        'form': form,
        'title': 'Blog',
        } 
        return render(request, 'blog/post_edit.html', context)