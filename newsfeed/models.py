from django.conf import settings
from django.db import models
class Post(models.Model):
    TYPES=[('lost','Lost'),('found','Found')]
    STATUSES=[('open','Open'),('returned','Returned'),('closed','Closed')]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts')
    community=models.ForeignKey('communities.Community',on_delete=models.CASCADE,related_name='posts')
    type=models.CharField(max_length=5,choices=TYPES)
    caption=models.CharField(max_length=180)


class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    content=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['created_at']

class Report(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='reports')
    reason=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['user','post'],name='one_report_per_post_user')]
