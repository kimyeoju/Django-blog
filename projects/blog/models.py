from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.hit += 1
        self.save()
        

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content


class HashTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name 