import graphene
from graphene_django import DjangoObjectType
from bbp.models import User, Post, Answer, Tag, Comment, Catagory, Like

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("is_superuser", "is_staff", "is_active")


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        exclude = ("post_answer_count", "post_hits")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer


class Query(graphene.ObjectType):
    post = graphene.List(PostType)
    user = graphene.List(UserType)
    answer = graphene.List(AnswerType)

    def resolve_user(self, info, **kwargs):
        return User.objects.all()

    def resolve_post(self, info, **kwargs):
        return Post.objects.all()

    def resolve_answer(self, info, **kwargs):
        return Answer.objects.all()