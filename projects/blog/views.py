from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# 글 목록 조회
class Index(View):
    def get(self, request):
        # Post 모델에서 전체 객체 가져오기
        post = Post.objects.all()
        # get 방식으로 호출된 url에서 page값을 가져올 때 사용 page값없이 호출된 경우에는 디폴트로 1이라는 값을 설정
        page = request.GET.get('page',1)
        # 첫번째 파라미터 post 게시물 전체를 의미하는 데이터, 두번째 파라미터는 5 페이지당 보여줄 게시물의 개수
        paginator = Paginator(post,5)
        # paginator을 이용하여 요청된 페이지(page)에 해당되는 페이징 객체(page_obj)생성 -> 장고 내부적으로 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회하도록 쿼리가 변경
        page_obj = paginator.get_page(page)
        context = {
            # posts는 page_obj 즉 5페이지의 데이터 조회
            'posts': page_obj,
            'title': 'Blog',
            'post_obj': post
        }
        return render(request, 'blog/post_list.html', context)


# 글 작성
class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
            'title': 'Blog'
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self,request):
        form = PostForm(request.POST, request.FILES) # files는 따로 request의 files로 속성을 지정
        
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
    
    def get(self, request, pk):
        post = Post.objects.prefetch_related('comment_set', 'hashtag_set').get(pk=pk)
        post.update_counter
        
        comments = post.comment_set.all()
        hashtags = post.hashtag_set.all()
        
        comment_form = CommentForm()
        hashtag_form = HashTagForm()
        
        context = {
            'title': 'Blog',
            'post_id' : pk,
            'post_title': post.title,
            'post_writer': post.writer,
            'post_content': post.content,
            'post_created_at': post.created_at,
            'post_hit': post.hit,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hashtag_form': hashtag_form,
            'post_imgfile' : post.imgfile
        }
        
        return render(request, 'blog/post_detail.html', context)
        

# 글 수정
class Update(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # 조건을 만족하는 object가 있으면 해당 object를 리턴하고, 없으면 404처리 첫번째 인자 Post에서 두번째 인자 해당 아이디의 post객체를 가져오는 것 
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post,
            # post객체 값을 넘겨주어야 더 정확함
            'title':'Blog'
        }
        return render(request, 'blog/post_edit.html',context)
    
    def post(self,request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST)
        
        if form.is_valid():
            # 폼의 입력값을 얻고 싶은 경우는 form.cleaned_data
            # form.cleaned_data로 접근하면 폼 인스턴스 내에서 clean함수를 통해 변환되었을 수도 있는 데이터를 가져오므로 좋은 접근
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
            # DetailView.get(self,request,post_id)로 정의했기 때문에 post_id로 attribute 선언해야함
        
        context = {
            'form': form,
            'title': 'Blog'
        }
        return render(request, 'blog/post_edit.html', context)


# 글 삭제
class Delete(View):
    
    def post(self,request,pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('blog:list')
    

# 댓글 작성
class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        
        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user
            
            try:
                comment = Comment.objects.create(post=post, content=content, writer=writer)
            except ObjectDoesNotExist as e:
                print('Post does not exist', str(e))
            
            except ValidationError as e:
                print('Validation error occurred', str(e))
            
            return redirect('blog:detail', pk=pk)
    
        hashtag_form = HashTagForm()
        
        context = {
            'title': 'Blog',
            'post_id' : pk,
            'comments' : post.comment_set.all(),
            'hashtags' : post.hashtag_set.all(),
            'comment_form' : form,
            'hashtag_form': hashtag_form
        }
        return render(request, 'blog/post_detail.html', context)


# 댓글 삭제
class CommentDelete(View):
    def post(self, request, pk): # comment_id
        comment = get_object_or_404(Comment, pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)


# 해시태그 작성
class HashTagWrite(LoginRequiredMixin, View):
    def post(self, request, pk): # post_id
        form = HashTagForm(request.POST)
        post = get_object_or_404(Post, pk=pk)
        
        if form.is_valid(): 
            name = form.cleaned_data['name']
            writer = request.user
            
            try:
                hashtag = HashTag.objects.create(post=post, name=name, writer=writer)
                
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
                
            except ValidationError as e:
                print('Validation error occurred', str(e))
            
            return redirect('blog:detail', pk=pk)
        
        comment_form = CommentForm()
        
        context = {
            'title': "Blog",
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': comment_form,
            'hashtag_form': form
        }
        return render(request,'blog/post_detail.html',context)


# 해시태그 삭제
class HashTagDelete(View):
    def post(self, request, pk): # hashtag_id
        hashtag = get_object_or_404(HashTag, pk=pk)
        post_id = hashtag.post.id
        hashtag.delete()
        return redirect('blog:detail', pk=post_id)
    

# 해시태그 검색
class PostSearch(View):
    def get(self, request, tag):
        print(f'request.GET: {request.GET}')
        posts = Post.objects.prefetch_related(
            'hashtag_set').filter(hashtag__name=tag)
        print(f'tag: {tag}')
        context = {
            'posts': posts,
        }
        return render(request, 'blog/post_list.html', context)