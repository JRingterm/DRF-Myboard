from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile

# Create your models here.
class Post(models.Model): #게시글 모델
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')#해당 유저의 게시물
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True) #해당 유저가 좋아요한 게시물
    published_date = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)#게시글에서 댓글을 불러오기 위해 nested serializer 개념 활용
    text = models.TextField()