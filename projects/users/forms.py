from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import get_user_model

User = get_user_model()
# model에서 User을 가지고옴
# 현재 활성화된 User 모델을 반환하며, 그렇지 않은 경우 User(default)모델을 반환 (객체 인스턴스를 반환)
# get_user_model()은 문자열이 아닌 클래스가 들어가야 하는 경우에 사용해주면 됨
# settings.AUTH_USER_MODEL 은 문자열

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User # get_user_model() - 객체 인스턴스 반환 / settings.AUTH_USER_MODEL - 세팅의 설정을 참고 문자열 반환
        fields = ['email']
        # 사용자에게 입력 받을 항목(폼)
        

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']