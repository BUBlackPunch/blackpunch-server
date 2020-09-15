from django.contrib import admin
from bbp.models import Post, Answer, Comment, Tag, Like, Catagory, Answer_like, Post_like

admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Catagory)
admin.site.register(Answer_like)
admin.site.register(Post_like)