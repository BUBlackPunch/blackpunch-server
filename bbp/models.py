from django.db import models
from user.models import User


class Catagory(models.Model):
    ca_name = models.CharField(max_length=100)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=225)
    post_content = models.TextField(blank=True)
    post_datatime = models.DateTimeField(auto_now_add=True)
    post_modify_datatime = models.DateTimeField(auto_now=True, null=True)
    post_answer_count = models.IntegerField(null=True)
    post_hits = models.IntegerField(null=True)
    po_like = models.ManyToManyField("Like", through='Post_like')


class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    as_content = models.TextField(blank=True)
    as_datetime = models.DateTimeField(auto_now_add=True)
    as_modify_datetime = models.DateTimeField(auto_now=True)
    as_like = models.ManyToManyField("Like", through='Answer_like')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    cm_content = models.CharField(max_length=200, blank=True)
    cm_datetime = models.DateTimeField(auto_now_add=True)
    cm_modify_datetime = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    post = models.ManyToManyField(Post, blank=True)
    answer = models.ManyToManyField(Answer, blank=True)
    tag_name = models.CharField(max_length=255)


class Like(models.Model):
    lk_datetime = models.DateTimeField(auto_now=True)
    li_ip = models.CharField(max_length=100)


class Answer_like(models.Model):
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post_like(models.Model):
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


