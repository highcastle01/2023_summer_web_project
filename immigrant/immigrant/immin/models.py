from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_no_special_characters
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={"unique":"이미 사용중인 닉네임입니다."},
    )
    def __str__(self):
        return self.email
    
class Post(models.Model):
    # 글의 제목, 내용 , 작성일, 마지막 수정일
    title = models.CharField(max_length=50)
    content = models.TextField()
    image1 = models.ImageField(upload_to="post_pics", blank=True)
    image2 = models.ImageField(upload_to="post_pics", blank=True)
    image3 = models.ImageField(upload_to="post_pics", blank=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
    
    def __str__(self):
        return self.title
    