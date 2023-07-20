from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
# Create your views here.

# 회원가입
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = RegisterForm()
        context = {
            'title':'Register',
            'form': form
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입을 통해 user의 정보들을 저장
            return redirect('users:login')
        context = {
            'title': 'Register',
            'form': form
        }
        return render(request, 'user/user_register.html', context)


# 로그인
class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            # boolean(True,False)값으로 반환 회원인지 아닌지 구별
            if user:
                login(request, user)
                return redirect('blog:list')
        # 에러가 들어간 폼
        context = {
            'form' : form
        }
        return render(request, 'user/user_login.html', context)
    

# 로그아웃
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')