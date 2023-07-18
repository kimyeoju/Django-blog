from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
# Create your models here.

# 유저 생성을 도와주는 헬퍼클래스
class UserManager(BaseUserManager):
    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('must have user email')
        now = timezone.localtime()
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now,
            **extra_fields
        ) # 일반 유저, 관리자 유저 메서드 실행시 입력 받은 값으로 구분
        user.set_password(password)
        user.save(using=self._db)
        # useing은 어떤 데이터베이스를 사용할 지 정해주는 매개변수 self._db는 현재 사용중인 데이터베이스를 의미
        return user
    
    def create_user(self, email, password, **extra_fields):
        # user을 생성하는 함수
        return self._create_user(email, password, False, False, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        # 관리자 user을 생성하는 함수
        return self._create_user(email,password, True, True, **extra_fields)
    

# 실제 모델이 상속받아 생성하는 클래스
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    # false값을 받도록 고정
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    data_joinded = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    # unique = True가 옵션으로 설정된 필드값으로 설정
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    # 필수로 받고 싶은 값 / username field값은 항상 기본적으로 요구하기 때문에 따로 명시하지 않아도 됨
    objects = UserManager()
    # 반드시 objects 값을 통해 헬퍼클래스를 지정해야 함
